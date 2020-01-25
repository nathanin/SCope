# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from scopeserver.dataserver.modules.gserver import s_pb2 as s__pb2


class MainStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.getCellColorByFeatures = channel.unary_unary(
        '/scope.Main/getCellColorByFeatures',
        request_serializer=s__pb2.CellColorByFeaturesRequest.SerializeToString,
        response_deserializer=s__pb2.CellColorByFeaturesReply.FromString,
        )
    self.getCellAUCValuesByFeatures = channel.unary_unary(
        '/scope.Main/getCellAUCValuesByFeatures',
        request_serializer=s__pb2.CellAUCValuesByFeaturesRequest.SerializeToString,
        response_deserializer=s__pb2.CellAUCValuesByFeaturesReply.FromString,
        )
    self.getCellMetaData = channel.unary_unary(
        '/scope.Main/getCellMetaData',
        request_serializer=s__pb2.CellMetaDataRequest.SerializeToString,
        response_deserializer=s__pb2.CellMetaDataReply.FromString,
        )
    self.getFeatures = channel.unary_unary(
        '/scope.Main/getFeatures',
        request_serializer=s__pb2.FeatureRequest.SerializeToString,
        response_deserializer=s__pb2.FeatureReply.FromString,
        )
    self.getCoordinates = channel.unary_unary(
        '/scope.Main/getCoordinates',
        request_serializer=s__pb2.CoordinatesRequest.SerializeToString,
        response_deserializer=s__pb2.CoordinatesReply.FromString,
        )
    self.getRegulonMetaData = channel.unary_unary(
        '/scope.Main/getRegulonMetaData',
        request_serializer=s__pb2.RegulonMetaDataRequest.SerializeToString,
        response_deserializer=s__pb2.RegulonMetaDataReply.FromString,
        )
    self.getMarkerGenes = channel.unary_unary(
        '/scope.Main/getMarkerGenes',
        request_serializer=s__pb2.MarkerGenesRequest.SerializeToString,
        response_deserializer=s__pb2.MarkerGenesReply.FromString,
        )
    self.getMyLooms = channel.unary_unary(
        '/scope.Main/getMyLooms',
        request_serializer=s__pb2.MyLoomsRequest.SerializeToString,
        response_deserializer=s__pb2.MyLoomsReply.FromString,
        )
    self.translateLassoSelection = channel.unary_unary(
        '/scope.Main/translateLassoSelection',
        request_serializer=s__pb2.TranslateLassoSelectionRequest.SerializeToString,
        response_deserializer=s__pb2.TranslateLassoSelectionReply.FromString,
        )
    self.getCellIDs = channel.unary_unary(
        '/scope.Main/getCellIDs',
        request_serializer=s__pb2.CellIDsRequest.SerializeToString,
        response_deserializer=s__pb2.CellIDsReply.FromString,
        )
    self.doGeneSetEnrichment = channel.unary_stream(
        '/scope.Main/doGeneSetEnrichment',
        request_serializer=s__pb2.GeneSetEnrichmentRequest.SerializeToString,
        response_deserializer=s__pb2.GeneSetEnrichmentReply.FromString,
        )
    self.getVmax = channel.unary_unary(
        '/scope.Main/getVmax',
        request_serializer=s__pb2.VmaxRequest.SerializeToString,
        response_deserializer=s__pb2.VmaxReply.FromString,
        )
    self.getUUID = channel.unary_unary(
        '/scope.Main/getUUID',
        request_serializer=s__pb2.UUIDRequest.SerializeToString,
        response_deserializer=s__pb2.UUIDReply.FromString,
        )
    self.getRemainingUUIDTime = channel.unary_unary(
        '/scope.Main/getRemainingUUIDTime',
        request_serializer=s__pb2.RemainingUUIDTimeRequest.SerializeToString,
        response_deserializer=s__pb2.RemainingUUIDTimeReply.FromString,
        )
    self.loomUploaded = channel.unary_unary(
        '/scope.Main/loomUploaded',
        request_serializer=s__pb2.LoomUploadedRequest.SerializeToString,
        response_deserializer=s__pb2.LoomUploadedReply.FromString,
        )
    self.getMyGeneSets = channel.unary_unary(
        '/scope.Main/getMyGeneSets',
        request_serializer=s__pb2.MyGeneSetsRequest.SerializeToString,
        response_deserializer=s__pb2.MyGeneSetsReply.FromString,
        )
    self.deleteUserFile = channel.unary_unary(
        '/scope.Main/deleteUserFile',
        request_serializer=s__pb2.DeleteUserFileRequest.SerializeToString,
        response_deserializer=s__pb2.DeleteUserFileReply.FromString,
        )
    self.downloadSubLoom = channel.unary_stream(
        '/scope.Main/downloadSubLoom',
        request_serializer=s__pb2.DownloadSubLoomRequest.SerializeToString,
        response_deserializer=s__pb2.DownloadSubLoomReply.FromString,
        )
    self.setAnnotationName = channel.unary_unary(
        '/scope.Main/setAnnotationName',
        request_serializer=s__pb2.SetAnnotationNameRequest.SerializeToString,
        response_deserializer=s__pb2.SetAnnotationNameReply.FromString,
        )
    self.setLoomHierarchy = channel.unary_unary(
        '/scope.Main/setLoomHierarchy',
        request_serializer=s__pb2.SetLoomHierarchyRequest.SerializeToString,
        response_deserializer=s__pb2.SetLoomHierarchyReply.FromString,
        )
    self.getORCIDiD = channel.unary_unary(
        '/scope.Main/getORCIDiD',
        request_serializer=s__pb2.getORCIDiDRequest.SerializeToString,
        response_deserializer=s__pb2.getORCIDiDReply.FromString,
        )
    self.getORCIDStatus = channel.unary_unary(
        '/scope.Main/getORCIDStatus',
        request_serializer=s__pb2.getORCIDStatusRequest.SerializeToString,
        response_deserializer=s__pb2.getORCIDStatusReply.FromString,
        )


class MainServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def getCellColorByFeatures(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCellAUCValuesByFeatures(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCellMetaData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getFeatures(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCoordinates(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRegulonMetaData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getMarkerGenes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getMyLooms(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def translateLassoSelection(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getCellIDs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def doGeneSetEnrichment(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getVmax(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUUID(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getRemainingUUIDTime(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def loomUploaded(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getMyGeneSets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def deleteUserFile(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def downloadSubLoom(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setAnnotationName(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def setLoomHierarchy(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getORCIDiD(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getORCIDStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_MainServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'getCellColorByFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.getCellColorByFeatures,
          request_deserializer=s__pb2.CellColorByFeaturesRequest.FromString,
          response_serializer=s__pb2.CellColorByFeaturesReply.SerializeToString,
      ),
      'getCellAUCValuesByFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.getCellAUCValuesByFeatures,
          request_deserializer=s__pb2.CellAUCValuesByFeaturesRequest.FromString,
          response_serializer=s__pb2.CellAUCValuesByFeaturesReply.SerializeToString,
      ),
      'getCellMetaData': grpc.unary_unary_rpc_method_handler(
          servicer.getCellMetaData,
          request_deserializer=s__pb2.CellMetaDataRequest.FromString,
          response_serializer=s__pb2.CellMetaDataReply.SerializeToString,
      ),
      'getFeatures': grpc.unary_unary_rpc_method_handler(
          servicer.getFeatures,
          request_deserializer=s__pb2.FeatureRequest.FromString,
          response_serializer=s__pb2.FeatureReply.SerializeToString,
      ),
      'getCoordinates': grpc.unary_unary_rpc_method_handler(
          servicer.getCoordinates,
          request_deserializer=s__pb2.CoordinatesRequest.FromString,
          response_serializer=s__pb2.CoordinatesReply.SerializeToString,
      ),
      'getRegulonMetaData': grpc.unary_unary_rpc_method_handler(
          servicer.getRegulonMetaData,
          request_deserializer=s__pb2.RegulonMetaDataRequest.FromString,
          response_serializer=s__pb2.RegulonMetaDataReply.SerializeToString,
      ),
      'getMarkerGenes': grpc.unary_unary_rpc_method_handler(
          servicer.getMarkerGenes,
          request_deserializer=s__pb2.MarkerGenesRequest.FromString,
          response_serializer=s__pb2.MarkerGenesReply.SerializeToString,
      ),
      'getMyLooms': grpc.unary_unary_rpc_method_handler(
          servicer.getMyLooms,
          request_deserializer=s__pb2.MyLoomsRequest.FromString,
          response_serializer=s__pb2.MyLoomsReply.SerializeToString,
      ),
      'translateLassoSelection': grpc.unary_unary_rpc_method_handler(
          servicer.translateLassoSelection,
          request_deserializer=s__pb2.TranslateLassoSelectionRequest.FromString,
          response_serializer=s__pb2.TranslateLassoSelectionReply.SerializeToString,
      ),
      'getCellIDs': grpc.unary_unary_rpc_method_handler(
          servicer.getCellIDs,
          request_deserializer=s__pb2.CellIDsRequest.FromString,
          response_serializer=s__pb2.CellIDsReply.SerializeToString,
      ),
      'doGeneSetEnrichment': grpc.unary_stream_rpc_method_handler(
          servicer.doGeneSetEnrichment,
          request_deserializer=s__pb2.GeneSetEnrichmentRequest.FromString,
          response_serializer=s__pb2.GeneSetEnrichmentReply.SerializeToString,
      ),
      'getVmax': grpc.unary_unary_rpc_method_handler(
          servicer.getVmax,
          request_deserializer=s__pb2.VmaxRequest.FromString,
          response_serializer=s__pb2.VmaxReply.SerializeToString,
      ),
      'getUUID': grpc.unary_unary_rpc_method_handler(
          servicer.getUUID,
          request_deserializer=s__pb2.UUIDRequest.FromString,
          response_serializer=s__pb2.UUIDReply.SerializeToString,
      ),
      'getRemainingUUIDTime': grpc.unary_unary_rpc_method_handler(
          servicer.getRemainingUUIDTime,
          request_deserializer=s__pb2.RemainingUUIDTimeRequest.FromString,
          response_serializer=s__pb2.RemainingUUIDTimeReply.SerializeToString,
      ),
      'loomUploaded': grpc.unary_unary_rpc_method_handler(
          servicer.loomUploaded,
          request_deserializer=s__pb2.LoomUploadedRequest.FromString,
          response_serializer=s__pb2.LoomUploadedReply.SerializeToString,
      ),
      'getMyGeneSets': grpc.unary_unary_rpc_method_handler(
          servicer.getMyGeneSets,
          request_deserializer=s__pb2.MyGeneSetsRequest.FromString,
          response_serializer=s__pb2.MyGeneSetsReply.SerializeToString,
      ),
      'deleteUserFile': grpc.unary_unary_rpc_method_handler(
          servicer.deleteUserFile,
          request_deserializer=s__pb2.DeleteUserFileRequest.FromString,
          response_serializer=s__pb2.DeleteUserFileReply.SerializeToString,
      ),
      'downloadSubLoom': grpc.unary_stream_rpc_method_handler(
          servicer.downloadSubLoom,
          request_deserializer=s__pb2.DownloadSubLoomRequest.FromString,
          response_serializer=s__pb2.DownloadSubLoomReply.SerializeToString,
      ),
      'setAnnotationName': grpc.unary_unary_rpc_method_handler(
          servicer.setAnnotationName,
          request_deserializer=s__pb2.SetAnnotationNameRequest.FromString,
          response_serializer=s__pb2.SetAnnotationNameReply.SerializeToString,
      ),
      'setLoomHierarchy': grpc.unary_unary_rpc_method_handler(
          servicer.setLoomHierarchy,
          request_deserializer=s__pb2.SetLoomHierarchyRequest.FromString,
          response_serializer=s__pb2.SetLoomHierarchyReply.SerializeToString,
      ),
      'getORCIDiD': grpc.unary_unary_rpc_method_handler(
          servicer.getORCIDiD,
          request_deserializer=s__pb2.getORCIDiDRequest.FromString,
          response_serializer=s__pb2.getORCIDiDReply.SerializeToString,
      ),
      'getORCIDStatus': grpc.unary_unary_rpc_method_handler(
          servicer.getORCIDStatus,
          request_deserializer=s__pb2.getORCIDStatusRequest.FromString,
          response_serializer=s__pb2.getORCIDStatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'scope.Main', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
