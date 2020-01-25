import React, { Component } from 'react';
import { withRouter, Link } from 'react-router-dom';
import { Icon, Label, Button, Menu, Image, Input, Popup, Checkbox} from 'semantic-ui-react';
import { BackendAPI } from './common/API';
import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import Bitly from 'bitlyapi';
const moment = require('moment');
const pako = require('pako');
let bitly = new Bitly(BITLY.token);

const timer = 60 * 1000;
const cookieName = 'SCOPE_UUID';


class AppHeader extends Component {
	static propTypes = {
		cookies: instanceOf(Cookies).isRequired
	}

	constructor(props) {
		super(props);
		this.state = {
			timeout: props.timeout,
			shortUrl: null,
			cookies: props.cookies,
			permalinkUUID: false,
			orcid_active: true
		}

		BackendAPI.getORCIDStatus((active) => { 
            this.setState({orcid_active: active})
        })
	}    
	
	openORCID = () => {
        window.open("https://orcid.org/oauth/authorize?client_id=" + ORCID.orcidAPIClientID + "&response_type=code&scope=/authenticate&show_login=false&redirect_uri=" + ORCID.orcidAPIRedirectURI, "_self", "toolbar=no, scrollbars=yes, width=500, height=600, top=500, left=500");
    }

	render() {
		const { match, location } = this.props;
		const { timeout, shortUrl } = this.state;
		let metadata = BackendAPI.getLoomMetadata(decodeURIComponent(match.params.loom));
		let menu = this.menuList(metadata);

		let orcid_logout = () => {
			this.props.cookies.remove("scope_orcid_name")
			this.props.cookies.remove("scope_orcid_id")
			this.props.cookies.remove("scope_orcid_uuid")
		}

		let orcid_info = () => {
			let orcid_name = this.props.cookies.get("scope_orcid_name")
			let orcid_id = this.props.cookies.get("scope_orcid_id")
			if (orcid_name && orcid_id) {
				return(
				<div>
					<Popup 
						position='bottom left'
						content={
							<div>You are authenticated with ORCID: {orcid_id}<p/>
							<Button onClick={() => orcid_logout()}>Log out</Button>
							<p/><b>By logging out you will no longer be able to annotate data. <br/>Your previous annotations and votes will remain.</b>
							</div>}
						trigger={<Image src="src/images/ORCIDiD_iconvector.svg" width="24" height="24" alt="ORCID iD icon" avatar/>} flowing hoverable/>
					Welcome {orcid_name}!
				</div>
				)
			} else {
				return(this.state.orcid_active && <Button id="connect-orcid-button" onClick={() => this.openORCID() }><img id="orcid-id-icon" src="https://orcid.org/sites/default/files/images/orcid_24x24.png" width="24" height="24" alt="ORCID iD icon"/>Authenticate with ORCID</Button>)
			}
		}

		return (
			<Menu secondary attached="top" className="vib" inverted>
				<Menu.Item>
					<Icon name="sidebar" onClick={this.toggleSidebar.bind(this)} className="pointer" title="Toggle sidebar" />
				</Menu.Item>

				{menu.map((item, i) => item.display &&
					<Menu.Item key={i}>
						<Link to={'/' + [match.params.uuid, match.params.loom, item.path].join('/')}>
							<Button basic active={match.params.page == item.path}>
								{item.icon &&
									<Icon name={item.icon} />
								}
								{item.title} &nbsp; {item.path == 'geneset' && <Label color='violet' size='mini'>beta</Label>}
							</Button>
						</Link>
					</Menu.Item>
				)}
				<Menu.Item>
					<Icon name="linkify" onClick={this.getPermalink.bind(this, this.state.permalinkUUID, false)} className="pointer" title="Get permalink" />
					{shortUrl &&
						<Label className="permalink">{shortUrl}</Label>}
					{shortUrl &&
						<Label>

							<Checkbox className="permalink" checked={this.state.permalinkUUID} onChange={this.getPermalink.bind(this, true)}
												data-tooltip="WARNING: Anyone that uses this link will have read and write access to this session but will be able to see all loom files in this session."
												data-position="bottom center"
												data-variation='tiny'/>
											{"      Include session UUID in permalink?"}
						</Label>

					}
				</Menu.Item>
				<Menu.Item className="orcidInfo">
					{orcid_info()}
				</Menu.Item>

				<Menu.Item className="sessionInfo">
					Your session will be deleted in {moment.duration(timeout).humanize()} &nbsp;
					<Icon name="info circle" inverted title="Our servers can only store that much data. Your files will be removed after the session times out." />
					<Button data-tooltip="Start with a new session ID. Your old ID will remain until its timeout expires, please store it if you would like to return. It cannot be recovered."
									data-position="bottom right"
									onClick={this.resetUUID.bind(this)}>
						Get new session

					</Button>
				</Menu.Item>
			</Menu>
		);
	}


	resetUUID() {
		const { history, cookies } = this.props;
		BackendAPI.getUUIDFromIP((uuid, timeRemaining) => {
			cookies.remove(cookieName);
			cookies.set(cookieName, uuid, { path: '/'});
			history.replace('/' + [uuid])
			BackendAPI.forceUpdate();

		})
	}

	componentWillMount() {
		this.timer = setInterval(() => {
			let timeout = this.state.timeout;
			timeout -= timer;
			this.setState({timeout});
			if (timeout <= 0) {
				clearInterval(this.timer);
				this.timer = null;
			}
		}, timer);
	}

	componentWillReceiveProps(nextProps) {
		if (DEBUG) console.log('componentWillReceiveProps', nextProps);
		const { timeout, metadata, match, history, loaded } = nextProps;
		this.setState({timeout: timeout});
		/*
		if (loaded) {
			let menu = this.menuList(metadata);
			menu.map((item) => {
				if ((item.path == match.params.page) && (!item.display))  {
					if (metadata) {
						history.replace('/'+ [match.params.uuid, match.params.loom, 'dataset' ].join('/'));
					} else {
						history.replace('/'+ [match.params.uuid, match.params.loom, 'welcome' ].join('/'));
					}
				}
			});
		}
		*/
	}

	componentWillUnmount() {
		if (this.timer)	clearInterval(this.timer);
	}

	toggleSidebar() {
		this.props.toggleSidebar();
		BackendAPI.setSidebarVisible(!BackendAPI.getSidebarVisible());
	}

	menuList(metadata) {
		return [
			{
				display: true,
				path: 'welcome',
				title: 'SCope',
				icon: 'home'
			},
			/*
			{
				display: metadata ? true : false,
				path: 'dataset',
				title: 'Dataset info',
				icon: false
			},
			*/
			{
				display: metadata ? true : false,
				path: 'gene',
				title: 'Gene',
				icon: false
			},
			{
				display: metadata ? true : false,
				path: 'geneset',
				title: 'Geneset',
				icon: false
			},
			{
				display: metadata && metadata.fileMetaData.hasRegulonsAUC ? true : false,
				path: 'regulon',
				title: 'Regulon',
				icon: false
			},
			{
				display: metadata ? true : false,
				path: 'compare',
				title: 'Compare',
				icon: false
			},
			{
				display: true,
				path: 'tutorial',
				title: 'Tutorial',
				icon: false
			},
			{
				display: true,
				path: 'about',
				title: 'About',
				icon: false
			},
		];
	}

	getPermalink(togglePermalinkUUID) {
		const { match } = this.props;
		if (togglePermalinkUUID) {
			let state = !this.state.permalinkUUID
			this.state.permalinkUUID = state
		}
		let j = JSON.stringify(BackendAPI.getExportObject(match.params), BackendAPI.getExportKeys());
		let d = pako.deflate(j, { to: 'string' });
		let b = encodeURIComponent(window.btoa(d).replace(/\//g,'$'));
		if (this.state.permalinkUUID) {
			var uuid = 'permalink__' + match.params.uuid
		} else {
			var uuid = 'permalink'
		}
		bitly.shorten(BITLY.baseURL + "/#/" + uuid + "/" + b)
		.then((result) => {
			this.setState({shortUrl: result.data.url});
			this.forceUpdate();
		}).then((error) => {
			if (error) {
				console.log(error);
			}
		});
	}
}

export default withRouter(AppHeader);
