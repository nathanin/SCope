from concurrent import futures
import time

import grpc
import s_pb2
import s_pb2_grpc

import loompy as lp
from loompy import LoomConnection
import hashlib
import os
import math
import numpy as np
import pandas as pd
import time
import json
import glob

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

hexarr = np.vectorize('{:02x}'.format)


class SCope(s_pb2_grpc.MainServicer):

    def __init__(self):
        self.active_loom_connections = {}

    @staticmethod
    def get_partial_md5_hash(file_path, last_n_kb):
        with open(file_path, 'rb') as f:
            f.seek(- last_n_kb * 1024, 2)
            return hashlib.md5(f.read()).hexdigest()

    def add_loom_connection(self, partial_md5_hash, loom):
        self.active_loom_connections[partial_md5_hash] = loom

    def load_loom_file(self, partial_md5_hash, loom_file_path):
        loom = lp.connect(loom_file_path)
        self.add_loom_connection(partial_md5_hash, loom)
        return loom

    def get_loom_connection(self, loom_file_path):
        if not os.path.exists(loom_file_path):
            raise ValueError('The file located at ' +
                             loom_file_path + ' does not exist.')
        # To check if the given file path is given specified url!
        partial_md5_hash = SCope.get_partial_md5_hash(
            loom_file_path, 10000)
        if partial_md5_hash in self.active_loom_connections:
            return self.active_loom_connections[partial_md5_hash]
        else:
            print("Debug: loading the loom file from " + loom_file_path + "...")
            return self.load_loom_file(partial_md5_hash, loom_file_path)

    def get_gene_expression(self, loom_file_path, gene_symbol, log_transform=True):
        loom = self.get_loom_connection(loom_file_path)
        print("Debug: getting expression of " + gene_symbol + "...")
        gene_expr = loom[loom.Gene == gene_symbol, :]
        if log_transform:
            print("Debug: log-transforming gene expression...")
            return np.log2(gene_expr + 1)[0]
        return gene_expr

    def get_features(self, loom_file_path, query):
        loom = self.get_loom_connection(loom_file_path)
        # Genes
        # Filter the genes by the query
        res = list(filter(lambda x: x.startswith(query), loom.Gene))
        # res_json = json.dumps({"gene": {"name": "gene", "results": list(map(lambda x: {"title":x,"description":"","image":"", "price":""}, res))}}, ensure_ascii=False)
        # print(res_json)
        print("Debug: " + str(len(res)) + " genes matching '" + query + "'")
        return res

    def get_coordinates(self, loom_file_path):
        loom = self.get_loom_connection(loom_file_path)
        return {"x": loom.col_attrs["_X"]
              , "y": loom.col_attrs["_Y"]}

    def getCellColorByFeatures(self, request, context):
        # request content
        #   - lfp   = .loom file path
        #   - e     = entries
        #   - f     = features
        #   - lte   = log transform expression
        start_time = time.time()
        n = 0
        # Feature 1
        if len(request.e[0]) > 0:
            # Get value of the given requested feature
            feature_1_val = self.get_gene_expression(
                loom_file_path=request.lfp, gene_symbol=request.e[0], log_transform=request.lte)
            # Normalize the value and convert to RGB values
            feature_1_val_norm = np.round(
                feature_1_val / (feature_1_val.max() * .8) * 255)
            n = feature_1_val_norm.size
        else:
            feature_1_val_norm = 0
        # Feature 2
        if len(request.e[1]) > 0:
            feature_2_val = self.get_gene_expression(
                loom_file_path=request.lfp, gene_symbol=request.e[1], log_transform=request.lte)
            feature_2_val_norm = np.round(
                feature_2_val / (feature_2_val.max() * .8) * 255)
        else:
            feature_2_val_norm = np.zeros(n)
        # Feature 3
        if len(request.e[2]) > 0:
            feature_3_val = self.get_gene_expression(
                loom_file_path=request.lfp, gene_symbol=request.e[2], log_transform=request.lte)
            feature_3_val_norm = np.round(
                feature_3_val / (feature_3_val.max() * .8) * 255)
        else:
            feature_3_val_norm = np.zeros(n)
        rgb_df = pd.DataFrame(data={'red': feature_1_val_norm.astype('u1')
                                  , 'green': feature_2_val_norm.astype('u1')
                                  , 'blue': feature_3_val_norm.astype('u1')})
        rgb_df = rgb_df[['red','green','blue']]
        rgb_arr = rgb_df.as_matrix()
        # Convert to RGB to hexadecimal format
        hex_arr = hexarr(rgb_arr)
        hex_vec = np.core.defchararray.add(np.core.defchararray.add(
            hex_arr[:, 0], hex_arr[:, 1]), hex_arr[:, 2])
        print("Debug: %s seconds elapsed ---" % (time.time() - start_time))
        return s_pb2.CellColorByFeaturesReply(v=hex_vec)

    def getFeatures(self, request, context):
        # request content
        #   - q   = query text
        return s_pb2.FeatureReply(v=self.get_features(request.lfp, request.q))

    def getCoordinates(self, request, context):
        # request content
        c = self.get_coordinates(request.lfp)
        return s_pb2.CoordinateReply(x=c["x"],y=c["y"])

    def getMyLooms(self, request, context):
        return s_pb2.MyLoomListReply(l=[f for f in os.listdir("my-looms/") if f.endswith('.loom')])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    s_pb2_grpc.add_MainServicer_to_server(SCope(), server)
    server.add_insecure_port('[::]:50052')
    print('Starting GServer on port 50052...')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
