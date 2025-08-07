<!DOCTYPE html><html lang="en-US" class="" data-primer><head><link href="https://a.slack-edge.com/73ef1f2/marketing/style/onetrust/onetrust_banner.css" rel="stylesheet" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><link href="https://a.slack-edge.com/bv1-13/legacy-style-libs-lato-2-compressed.b4a5b5cd94ce5aee6359.min.css" rel="stylesheet" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><link href="https://a.slack-edge.com/bv1-13/marketing-style-generic-typography-avantgarde.e5bf1218673e1b980835.min.css" rel="stylesheet" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><link href="https://a.slack-edge.com/bv1-13/marketing-style-generic-typography-sfsans.663a8f35624c9f33608d.min.css" rel="stylesheet" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><link rel="canonical" href="https://slack.com">

<link rel="alternate" hreflang="en-us" href="https://slack.com">

<link rel="alternate" hreflang="en-au" href="https://slack.com/intl/en-au">

<link rel="alternate" hreflang="en-gb" href="https://slack.com/intl/en-gb">

<link rel="alternate" hreflang="en-in" href="https://slack.com/intl/en-in">

<link rel="alternate" hreflang="fr-ca" href="https://slack.com/intl/fr-ca">

<link rel="alternate" hreflang="fr-fr" href="https://slack.com/intl/fr-fr">

<link rel="alternate" hreflang="de-de" href="https://slack.com/intl/de-de">

<link rel="alternate" hreflang="es-es" href="https://slack.com/intl/es-es">

<link rel="alternate" hreflang="es" href="https://slack.com/intl/es-la">

<link rel="alternate" hreflang="ja-jp" href="https://slack.com/intl/ja-jp">

<link rel="alternate" hreflang="pt-br" href="https://slack.com/intl/pt-br">

<link rel="alternate" hreflang="ko-kr" href="https://slack.com/intl/ko-kr">

<link rel="alternate" hreflang="it-it" href="https://slack.com/intl/it-it">

<link rel="alternate" hreflang="zh-cn" href="https://slack.com/intl/zh-cn">

<link rel="alternate" hreflang="zh-tw" href="https://slack.com/intl/zh-tw">

<link rel="alternate" hreflang="x-default" href="https://slack.com">

<script>window.ts_endpoint_url = "https:\/\/slack.com\/beacon\/timing";(function(e) {
	var n=Date.now?Date.now():+new Date,r=e.performance||{},t=[],a={},i=function(e,n){for(var r=0,a=t.length,i=[];a>r;r++)t[r][e]==n&&i.push(t[r]);return i},o=function(e,n){for(var r,a=t.length;a--;)r=t[a],r.entryType!=e||void 0!==n&&r.name!=n||t.splice(a,1)};r.now||(r.now=r.webkitNow||r.mozNow||r.msNow||function(){return(Date.now?Date.now():+new Date)-n}),r.mark||(r.mark=r.webkitMark||function(e){var n={name:e,entryType:"mark",startTime:r.now(),duration:0};t.push(n),a[e]=n}),r.measure||(r.measure=r.webkitMeasure||function(e,n,r){n=a[n].startTime,r=a[r].startTime,t.push({name:e,entryType:"measure",startTime:n,duration:r-n})}),r.getEntriesByType||(r.getEntriesByType=r.webkitGetEntriesByType||function(e){return i("entryType",e)}),r.getEntriesByName||(r.getEntriesByName=r.webkitGetEntriesByName||function(e){return i("name",e)}),r.clearMarks||(r.clearMarks=r.webkitClearMarks||function(e){o("mark",e)}),r.clearMeasures||(r.clearMeasures=r.webkitClearMeasures||function(e){o("measure",e)}),e.performance=r,"function"==typeof define&&(define.amd||define.ajs)&&define("performance",[],function(){return r}) // eslint-disable-line
})(window);</script><script>

(function () {
	
	window.TSMark = function (mark_label) {
		if (!window.performance || !window.performance.mark) return;
		performance.mark(mark_label);
	};
	window.TSMark('start_load');

	
	window.TSMeasureAndBeacon = function (measure_label, start_mark_label) {
		if (!window.performance || !window.performance.mark || !window.performance.measure) {
			return;
		}

		performance.mark(start_mark_label + '_end');

		try {
			performance.measure(measure_label, start_mark_label, start_mark_label + '_end');
			window.TSBeacon(measure_label, performance.getEntriesByName(measure_label)[0].duration);
		} catch (e) {
			
		}
	};

	
	if ('sendBeacon' in navigator) {
		window.TSBeacon = function (label, value) {
			var endpoint_url = window.ts_endpoint_url || 'https://slack.com/beacon/timing';
			navigator.sendBeacon(
				endpoint_url + '?data=' + encodeURIComponent(label + ':' + value),
				'',
			);
		};
	} else {
		window.TSBeacon = function (label, value) {
			var endpoint_url = window.ts_endpoint_url || 'https://slack.com/beacon/timing';
			new Image().src = endpoint_url + '?data=' + encodeURIComponent(label + ':' + value);
		};
	}
})();
</script><script>window.TSMark('step_load');</script><script>
(function () {
	function throttle(callback, intervalMs) {
		var wait = false;

		return function () {
			if (!wait) {
				callback.apply(null, arguments);
				wait = true;
				setTimeout(function () {
					wait = false;
				}, intervalMs);
			}
		};
	}

	function getGenericLogger() {
		return {
			warn: (msg) => {
				
				if (window.console && console.warn) return console.warn(msg);
			},
			error: (msg) => {
				if (!msg) return;

				if (window.TSBeacon) return window.TSBeacon(msg, 1);

				
				if (window.console && console.warn) return console.warn(msg);
			},
		};
	}

	function globalErrorHandler(evt) {
		if (!evt) return;

		
		var details = '';

		var node = evt.srcElement || evt.target;

		var genericLogger = getGenericLogger();

		
		
		
		
		if (node && node.nodeName) {
			var nodeSrc = '';
			if (node.nodeName === 'SCRIPT') {
				nodeSrc = node.src || 'unknown';
				var errorType = evt.type || 'error';

				
				details = `[${errorType}] from script at ${nodeSrc} (failed to load?)`;
			} else if (node.nodeName === 'IMG') {
				nodeSrc = node.src || node.currentSrc;

				genericLogger.warn(`<img> fired error with url = ${nodeSrc}`);
				return;
			}
		}

		
		if (evt.error && evt.error.stack) {
			details += ` ${evt.error.stack}`;
		}

		if (evt.filename) {
			
			var fileName = evt.filename;
			var lineNo = evt.lineno;
			var colNo = evt.colno;

			details += ` from ${fileName}`;

			
			if (lineNo) {
				details += ` @ line ${lineNo}, col ${colNo}`;
			}
		}

		var msg;

		
		if (evt.error && evt.error.stack) {
			
			msg = details;
		} else {
			
			msg = `${evt.message || ''} ${details}`;
		}

		
		if (msg && msg.replace) msg = msg.replace(/\s+/g, ' ').trim();

		if (!msg || !msg.length) {
			if (node) {
				var nodeName = node.nodeName || 'unknown';

				
				
				
				if (nodeName === 'VIDEO') {
					return;
				}

				msg = `error event from node of ${nodeName}, no message provided?`;
			} else {
				msg = 'error event fired, no relevant message or node found';
			}
		}

		var logPrefix = 'ERROR caught in js/inline/register_global_error_handler';

		msg = `${logPrefix} - ${msg}`;

		genericLogger.error(msg);
	}

	
	
	
	var capture = true;

	
	var throttledHandler = throttle(globalErrorHandler, 10000);

	window.addEventListener('error', throttledHandler, capture);
})();
</script><script type="text/javascript" crossorigin="anonymous" src="https://a.slack-edge.com/bv1-13/manifest.8fd9396b7d1284694393.primer.min.js" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null"></script><noscript><meta http-equiv="refresh" content="0; URL=/?redir=%2Ffiles-pri%2FTS70V2213-F0987EF8C4W%2Fdownload%2Flogin.py&amp;nojsmode=1"></noscript><script type="text/javascript">var safe_hosts = ['app.optimizely.com', 'tinyspeck.dev.slack.com'];

if (self !== top && safe_hosts.indexOf(top.location.host) === -1) {
	window.document.write(
		'\u003Cstyle>body * {display:none !important;}\u003C/style>\u003Ca href="#" onclick=' +
			'"top.location.href=window.location.href" style="display:block !important;padding:10px">Go to Slack.com\u003C/a>'
	);
}

(function() {
	var timer;
	if (self !== top && safe_hosts.indexOf(top.location.host) === -1) {
		timer = window.setInterval(function() {
			if (window) {
				try {
					var pageEl = document.getElementById('page');
					var clientEl = document.getElementById('client-ui');
					var sectionEls = document.querySelectorAll('nav, header, section');

					pageEl.parentNode.removeChild(pageEl);
					clientEl.parentNode.removeChild(clientEl);
					for (var i = 0; i < sectionEls.length; i++) {
						sectionEls[i].parentNode.removeChild(sectionEls[i]);
					}
					window.TS = null;
					window.TD = null;
					window.clearInterval(timer);
				} catch (e) {}
			}
		}, 200);
	}
})();</script><meta name="facebook-domain-verification" content="chiwsajpoybn2cnqyj9w8mvrey56m0"><script type="text/javascript">
document.addEventListener("DOMContentLoaded", function(e) {
	var gtmDataLayer = window.dataLayer || [];
	var gtmTags = document.querySelectorAll('*[data-gtm-click]');
	var gtmClickHandler = function(c) {
		var gtm_events = this.getAttribute('data-gtm-click');
		if (!gtm_events) return;
		var gtm_events_arr = gtm_events.split(",");
		for(var e=0; e < gtm_events_arr.length; e++) {
			var ev = gtm_events_arr[e].trim();
			gtmDataLayer.push({ 'event': ev });
		}
	};
	for(var g=0; g < gtmTags.length; g++){
		var elem = gtmTags[g];
		elem.addEventListener('click', gtmClickHandler);
	}
});
</script><script type="text/javascript">
(function(e,c,b,f,d,g,a){e.SlackBeaconObject=d;
e[d]=e[d]||function(){(e[d].q=e[d].q||[]).push([1*new Date(),arguments])};
e[d].l=1*new Date();g=c.createElement(b);a=c.getElementsByTagName(b)[0];
g.async=1;g.src=f;a.parentNode.insertBefore(g,a)
})(window,document,"script","https://a.slack-edge.com/bv1-13/slack_beacon.10d18d9f8a63b0cd84b0.min.js","sb");
window.sb('set', 'token', '3307f436963e02d4f9eb85ce5159744c');
window.sb('track', 'pageview');
</script><script src="https://cdn.cookielaw.org/scripttemplates/otSDKStub.js" data-document-language="true" data-domain-script="3bcd90cf-1e32-46d7-adbd-634f66b65b7d"></script><script>window.OneTrustLoaded = true;</script><script>
window.dataLayer = window.dataLayer || [];

function afterConsentScripts() {
	window.TD.analytics.doPush();

	const bottomBannerEl = document.querySelector('.c-announcement-banner-bottom');
	if (bottomBannerEl !== null) {
		bottomBannerEl.classList.remove('c-announcement-banner-bottom-invisible');
	}
}



var initOneTrustReady = false;
function OptanonWrapper() {
	gtag('consent', "update", {"ad_storage":"denied","ad_user_data":"denied","ad_personalization":"denied","personalization_storage":"denied","analytics_storage":"denied","functionality_storage":"denied","security_storage":"denied"});
	window.dataLayer.push({'event': 'OneTrustReady'});
	if (!initOneTrustReady) {
		document.dispatchEvent(new CustomEvent('OneTrustReady'));
		loadGTM();
		initOneTrustReady = true;
	}

	if (!Optanon.GetDomainData().ShowAlertNotice || false) {
		afterConsentScripts();
	} else {
		document.querySelector('#onetrust-accept-btn-handler').focus()
	}
	Optanon.OnConsentChanged(function() {
		afterConsentScripts();
	});

}</script><script type="text/javascript">var TS_last_log_date = null;
var TSMakeLogDate = function() {
	var date = new Date();

	var y = date.getFullYear();
	var mo = date.getMonth()+1;
	var d = date.getDate();

	var time = {
	  h: date.getHours(),
	  mi: date.getMinutes(),
	  s: date.getSeconds(),
	  ms: date.getMilliseconds()
	};

	Object.keys(time).map(function(moment, index) {
		if (moment == 'ms') {
			if (time[moment] < 10) {
				time[moment] = time[moment]+'00';
			} else if (time[moment] < 100) {
				time[moment] = time[moment]+'0';
			}
		} else if (time[moment] < 10) {
			time[moment] = '0' + time[moment];
		}
	});

	var str = y + '/' + mo + '/' + d + ' ' + time.h + ':' + time.mi + ':' + time.s + '.' + time.ms;
	if (TS_last_log_date) {
		var diff = date-TS_last_log_date;
		//str+= ' ('+diff+'ms)';
	}
	TS_last_log_date = date;
	return str+' ';
}

var parseDeepLinkRequest = function(code) {
	var m = code.match(/"id":"([CDG][A-Z0-9]{8,})"/);
	var id = m ? m[1] : null;

	m = code.match(/"team":"(T[A-Z0-9]{8,})"/);
	var team = m ? m[1] : null;

	m = code.match(/"message":"([0-9]+\.[0-9]+)"/);
	var message = m ? m[1] : null;

	return { id: id, team: team, message: message };
}

if ('rendererEvalAsync' in window) {
	var origRendererEvalAsync = window.rendererEvalAsync;
	window.rendererEvalAsync = function(blob) {
		try {
			var data = JSON.parse(decodeURIComponent(atob(blob)));
			if (data.code.match(/handleDeepLink/)) {
				var request = parseDeepLinkRequest(data.code);
				if (!request.id || !request.team || !request.message) return;

				request.cmd = 'channel';
				TSSSB.handleDeepLinkWithArgs(JSON.stringify(request));
				return;
			} else {
				origRendererEvalAsync(blob);
			}
		} catch (e) {
		}
	}
}</script><script type="text/javascript">var TSSSB = {
	call: function() {
		return false;
	}
};</script><title>Slack</title><meta name="referrer" content="no-referrer"><meta name="author" content="Slack"><meta name="description" content=""><meta name="keywords" content=""><meta name="HandheldFriendly" content="true"><meta name="viewport" content="width=device-width, initial-scale=1.0"></head><body class="full_height"><div id="page_contents"><div id="props_node" data-props="{&quot;loggedInTeams&quot;:[],&quot;entryPoint&quot;:&quot;&quot;,&quot;isPaidTeam&quot;:false,&quot;teamName&quot;:&quot;AiimTech&quot;,&quot;teamDomain&quot;:&quot;aiimtech&quot;,&quot;encodedTeamId&quot;:&quot;TS70V2213&quot;,&quot;emailJustSent&quot;:false,&quot;shouldRedirect&quot;:true,&quot;redirectURL&quot;:&quot;\/files-pri\/TS70V2213-F0987EF8C4W\/download\/login.py&quot;,&quot;redirectQs&quot;:&quot;\/?redir=%2Ffiles-pri%2FTS70V2213-F0987EF8C4W%2Fdownload%2Flogin.py&quot;,&quot;remember&quot;:false,&quot;hasRemember&quot;:true,&quot;noSSO&quot;:false,&quot;crumbValue&quot;:&quot;s-1753947388-8710e69548240deb21fa88784895412673c81347315ab2c8e7d28f9c88602869-\u2603&quot;,&quot;isSSB&quot;:false,&quot;isSSBSignIn&quot;:false,&quot;isSSBSonicSignIn&quot;:false,&quot;SSBVersion&quot;:&quot;&quot;,&quot;hasEmailError&quot;:false,&quot;emailValue&quot;:&quot;&quot;,&quot;hasPasswordError&quot;:false,&quot;isMobileBrowser&quot;:true,&quot;hasAuthReloginFlow&quot;:false,&quot;hasRateLimit&quot;:false,&quot;recaptchaSitekey&quot;:&quot;6LcQQiYUAAAAADxJHrihACqD5wf3lksm9jbnRY5k&quot;,&quot;hasSmsRateLimit&quot;:false,&quot;forgotPasswordLink&quot;:&quot;\/forgot&quot;,&quot;showSignupEmailLink&quot;:false,&quot;getStartedLink&quot;:&quot;https:\/\/slack.com\/get-started?entry_point=login#\/find&quot;,&quot;isSSOAuthMode&quot;:false,&quot;isNormalAuthMode&quot;:true,&quot;signinUrl&quot;:&quot;https:\/\/slack.com\/signin&quot;,&quot;signinFindUrl&quot;:&quot;https:\/\/slack.com\/signin\/find&quot;,&quot;ssbRelogin&quot;:&quot;&quot;,&quot;isLoggedOutSSOMaybeRequired&quot;:false,&quot;isLoggedOutRedirect&quot;:true,&quot;teamAuthMode&quot;:null,&quot;authModeGoogle&quot;:&quot;google&quot;,&quot;samlProviderLabel&quot;:null,&quot;errorSource&quot;:&quot;&quot;,&quot;errorMissing&quot;:false,&quot;errorNoUser&quot;:false,&quot;errorDeleted&quot;:false,&quot;errorPassword&quot;:false,&quot;errorSSONoOwner&quot;:false,&quot;errorSSONonRA&quot;:false,&quot;errorTwoFactorWrong&quot;:false,&quot;errorSmsRateLimit&quot;:false,&quot;errorConfirmed&quot;:false,&quot;errorNoPassword&quot;:false,&quot;errorTwoFactorState&quot;:false,&quot;hasEmailOnDomain&quot;:true,&quot;truncatedEmailDomains&quot;:null,&quot;truncatedEmailDomainsCount&quot;:0,&quot;formattedEmailDomains&quot;:&quot;@aiimtech.com&quot;,&quot;isReloginFlow&quot;:false,&quot;downloadLinkSigninCTA&quot;:{&quot;linkUrl&quot;:&quot;https:\/\/play.google.com\/store\/apps\/details?id=com.Slack&amp;listing=slackmobileweb&quot;,&quot;isDownload&quot;:true},&quot;twoFactorRequired&quot;:false,&quot;usingBackup&quot;:null,&quot;twoFactorType&quot;:null,&quot;twoFactorBackupType&quot;:null,&quot;twoFactorRequiredML&quot;:null,&quot;authcodeInputType&quot;:&quot;tel&quot;,&quot;backupPhoneNumber&quot;:null,&quot;forgotPasswordError&quot;:&quot;&quot;,&quot;resetLinkSent&quot;:false,&quot;userOauth&quot;:{&quot;apple&quot;:{&quot;enabled&quot;:true,&quot;redirect_url&quot;:&quot;https:\/\/aiimtech.slack.com\/workspace-signin\/oauth\/apple\/start?redir=%2Ffiles-pri%2FTS70V2213-F0987EF8C4W%2Fdownload%2Flogin.py&amp;is_ssb_browser_signin=&quot;},&quot;google&quot;:{&quot;enabled&quot;:true,&quot;redirect_url&quot;:&quot;https:\/\/aiimtech.slack.com\/workspace-signin\/oauth\/google\/start?redir=%2Ffiles-pri%2FTS70V2213-F0987EF8C4W%2Fdownload%2Flogin.py&amp;is_ssb_browser_signin=&quot;}},&quot;isUrgentBannerExpOn&quot;:false,&quot;isWarningBannerExpOn&quot;:true,&quot;signInWithPassword&quot;:false}"></div></div><script type="text/javascript">
/**
 * A placeholder function that the build script uses to
 * replace file paths with their CDN versions.
 *
 * @param {String} file_path - File path
 * @returns {String}
 */
function vvv(file_path) {
		 var vvv_warning = 'You cannot use vvv on dynamic values. Please make sure you only pass in static file paths.'; if (window.TS && window.TS.warn) { window.TS.warn(vvv_warning); } else { console.warn(vvv_warning); } 
	return file_path;
}

var cdn_url = "https:\/\/a.slack-edge.com";
var vvv_abs_url = "https:\/\/slack.com\/";
var inc_js_setup_data = {
	emoji_sheets: {
		apple: 'https://a.slack-edge.com/80588/img/emoji_2017_12_06/sheet_apple_64_indexed_256.png',
		google: 'https://a.slack-edge.com/80588/img/emoji_2017_12_06/sheet_google_64_indexed_256.png',
	},
};
</script><script nonce="" type="text/javascript">	// common boot_data
	var boot_data = {"cdn":{"edges":["https:\/\/a.slack-edge.com\/","https:\/\/b.slack-edge.com\/","https:\/\/a.slack-edge.com\/"],"avatars":"https:\/\/ca.slack-edge.com\/","downloads":"https:\/\/downloads.slack-edge.com\/","files":"https:\/\/slack-files.com\/"},"feature_builder_story_step":false,"feature_olug_remove_required_workspace_setting":false,"feature_file_threads":true,"feature_broadcast_indicator":true,"feature_sonic_emoji":true,"feature_attachments_inline":false,"feature_desktop_symptom_events":false,"feature_gdpr_user_join_tos":true,"feature_user_invite_tos_april_2018":true,"feature_channel_mgmt_message_count":false,"feature_channel_exports":false,"feature_allow_intra_word_formatting":true,"feature_slim_scrollbar":false,"feature_edge_upload_proxy_check":false,"feature_set_tz_automatically":true,"feature_attachments_v2":true,"feature_beacon_js_errors":true,"feature_user_app_disable_speed_bump":true,"feature_apps_manage_permissions_scope_changes":true,"feature_ia_member_profile":true,"feature_desktop_reload_on_generic_error":true,"feature_desktop_extend_app_menu":true,"feature_desktop_restart_service_worker":false,"feature_wta_stop_creation":true,"feature_admin_email_change_confirm":false,"feature_improved_email_rendering":true,"feature_recent_desktop_files":true,"feature_cea_allowlist_changes":false,"feature_cea_channel_management":true,"feature_cea_admin_controls":false,"feature_cea_allowlist_changes_plus":false,"feature_ia_layout":true,"feature_threaded_call_block":true,"feature_enterprise_mobile_device_check":true,"feature_trace_jq_init":true,"feature_seven_days_email_update":true,"feature_channel_sections":true,"feature_show_email_forwarded_by":false,"feature_mpdm_audience_expansion":true,"feature_remove_email_preview_link":true,"feature_desktop_enable_tslog":false,"feature_email_determine_charset":true,"feature_no_deprecation_in_updater":false,"feature_pea_domain_allowlist":true,"feature_composer_auth_admin":true,"experiment_assignments":{"phone_number_de":{"experiment_id":"7168806134229","type":"visitor","group":"treatment","schedule_ts":1716908444,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_fr":{"experiment_id":"7157169096183","type":"visitor","group":"treatment","schedule_ts":1716912646,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_au":{"experiment_id":"7168837725445","type":"visitor","group":"treatment","schedule_ts":1716912663,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_br":{"experiment_id":"7256414077620","type":"visitor","group":"treatment","schedule_ts":1719244830,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_it":{"experiment_id":"7250980705925","type":"visitor","group":"treatment","schedule_ts":1719253456,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_es":{"experiment_id":"7266548128369","type":"visitor","group":"treatment","schedule_ts":1719253482,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_ca":{"experiment_id":"7256320861108","type":"visitor","group":"treatment","schedule_ts":1718813429,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"versionify_url_for_invites":{"experiment_id":"9239948574183","type":"visitor","group":"on","trigger":"hash_visitor","schedule_ts":1753809230,"log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"modular_pages_phase_3":{"experiment_id":"9032745384455","type":"visitor","group":"on","schedule_ts":1753834662,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"ratelimit_migrate_to_quota":{"experiment_id":"9222799109489","type":"visitor","group":"on","schedule_ts":1752856347,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"workflow_builder":{"experiment_id":"9193723819463","type":"visitor","group":"on","schedule_ts":1753792231,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketing_pricing_page_meta":{"experiment_id":"9253895333078","type":"visitor","group":"on","schedule_ts":1753723294,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_pt":{"experiment_id":"7276731000896","type":"visitor","group":"treatment","schedule_ts":1719253468,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_ko":{"experiment_id":"7276620382240","type":"visitor","group":"treatment","schedule_ts":1719852648,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_ie":{"experiment_id":"7441623906036","type":"visitor","group":"treatment","schedule_ts":1721414251,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"phone_number_jp":{"experiment_id":"7174178940996","type":"visitor","group":"treatment","schedule_ts":1716583378,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"agent_demo_contact":{"experiment_id":"9180003200743","type":"visitor","group":"on","schedule_ts":1753365260,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"enterprise_search_july15":{"experiment_id":"9087784591047","type":"visitor","group":"on","schedule_ts":1752754218,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"dotcom_mobile_attribution":{"experiment_id":"9172289627489","type":"visitor","group":"on","schedule_ts":1752614172,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"partner_promos_pnp":{"experiment_id":"8997210765159","type":"visitor","group":"on","schedule_ts":1750106249,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"july15_launch":{"experiment_id":"9119464602736","type":"visitor","group":"on","schedule_ts":1752754244,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"daily_limit_confirmation_code":{"experiment_id":"8869063590709","type":"visitor","group":"on","schedule_ts":1749751884,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"activation_browser_deprecation_warning_july_2025":{"experiment_id":"9167270708324","type":"visitor","group":"on","schedule_ts":1752602320,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"dreamforce_promo":{"experiment_id":"9163466061797","type":"visitor","group":"on","schedule_ts":1752590157,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"adaptive_video_test":{"experiment_id":"9192971447505","type":"visitor","group":"on","schedule_ts":1752524529,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketplace_popularity":{"experiment_id":"9111411283031","type":"visitor","group":"on","schedule_ts":1752514838,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"july1_launch":{"experiment_id":"9111164109201","type":"visitor","group":"on","schedule_ts":1751403911,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"mobile_web_signup":{"experiment_id":"9159597839650","type":"visitor","group":"treatment","schedule_ts":1751984259,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"cust_acq_templates_faq":{"experiment_id":"8842237418498","type":"visitor","group":"on","schedule_ts":1752075211,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"apidocs_search_local_only_v2":{"experiment_id":"9128237007047","type":"visitor","group":"on","schedule_ts":1751574359,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"miro_marketplace":{"experiment_id":"8704952792931","type":"visitor","group":"on","schedule_ts":1750982806,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"channels_update":{"experiment_id":"8954244938662","type":"visitor","group":"on","schedule_ts":1748951415,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"cust_acq_pricing_highlight_bus_plus":{"experiment_id":"8885121789856","type":"visitor","group":"control","trigger":"hash_visitor","schedule_ts":1750266608,"log_exposures":true,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"spam_email_recaptcha_v3":{"experiment_id":"8890538137939","type":"visitor","group":"on","schedule_ts":1749589661,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"slack_marketplace_modern":{"experiment_id":"8041385254518","type":"visitor","group":"on","schedule_ts":1749135463,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"pro_discount_btf":{"experiment_id":"8830623175587","type":"visitor","group":"control","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"homepage_hero_atf_copy":{"experiment_id":"8709043044887","type":"visitor","group":"treatment_a","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"marketing_aff":{"experiment_id":"5743479690565","type":"visitor","group":"on","schedule_ts":1749577342,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"signin_design_refresh":{"experiment_id":"8656625636818","type":"visitor","group":"on","schedule_ts":1746462640,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"enterprise_search_demo":{"experiment_id":"8892730774644","type":"visitor","group":"on","schedule_ts":1749226177,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"sem_lp_pricing_grid_ga":{"experiment_id":"8938536505986","type":"visitor","group":"on","schedule_ts":1749144872,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"creator_landing_view_refactor":{"experiment_id":"8986548312550","type":"visitor","group":"on","schedule_ts":1749141715,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"enable_optimizely_webapp":{"experiment_id":"7891954779538","type":"visitor","group":"on","schedule_ts":1747945849,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"sandbox_password_free_signin":{"experiment_id":"8766535145014","type":"visitor","group":"on","schedule_ts":1746821450,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"innovations_lp":{"experiment_id":"8253871971107","type":"visitor","group":"on","schedule_ts":1746643793,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"enterprise_search_lp":{"experiment_id":"8787098737047","type":"visitor","group":"on","schedule_ts":1746641312,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"aswebauth_cookie_session":{"experiment_id":"7920012625699","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"spam_email_recaptcha":{"experiment_id":"8449964217459","type":"visitor","group":"on","schedule_ts":1746141854,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"limit_confirmation_code_for_alias_email":{"experiment_id":"8695671490005","type":"visitor","group":"on","schedule_ts":1744822321,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"april_pages2":{"experiment_id":"8743286716099","type":"visitor","group":"on","schedule_ts":1745440781,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"mris_extension":{"experiment_id":"4746206947365","type":"visitor","group":"on","schedule_ts":1706216371,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"on24_extension":{"experiment_id":"4772019824211","type":"visitor","group":"on","schedule_ts":1675891595,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"solution_gallery":{"experiment_id":"7805433315095","type":"visitor","group":"on","schedule_ts":1730293827,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"ai_paid_campaign":{"experiment_id":"7385757537713","type":"visitor","group":"on","schedule_ts":1721664156,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"us_logos_team_creation_experiment":{"experiment_id":"8641303092306","type":"visitor","group":"treatment","trigger":"hash_visitor","schedule_ts":1742936666,"log_exposures":true,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"sticky_fyp_cta":{"experiment_id":"8281275470644","type":"visitor","group":"control","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"downloads_launch":{"experiment_id":"8552687986532","type":"visitor","group":"on","schedule_ts":1741711036,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"add_team_creation_flow_segmentation":{"experiment_id":"8399073017011","type":"visitor","group":"on","schedule_ts":1741620581,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"hp_mobile_revamp_fy26":{"experiment_id":"8427344932433","type":"visitor","group":"on","schedule_ts":1741262676,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"oauth_domain_signin_fix":{"experiment_id":"7214626556485","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"activation_enterprise_signin_primer":{"experiment_id":"6443324713893","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"sf_fonts_latin":{"experiment_id":"7577927212402","type":"visitor","group":"on","schedule_ts":1739573433,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"sf_fonts_cjk":{"experiment_id":"7575044373701","type":"visitor","group":"on","schedule_ts":1739573413,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"slack_developer_program_trailhead_optimization":{"experiment_id":"8018607835799","type":"visitor","group":"on","schedule_ts":1737049638,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"screen_text_2fa":{"experiment_id":"7846147603012","type":"visitor","group":"on","schedule_ts":1734375504,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"app_directory_connectors_collection":{"experiment_id":"6321714753558","type":"visitor","group":"on","schedule_ts":1705448247,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"app_directory_connectors":{"experiment_id":"6144504493874","type":"visitor","group":"treatment","schedule_ts":1705354312,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"app_directory_coral":{"experiment_id":"8121125935588","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"marketplace_add":{"experiment_id":"7940445156581","type":"visitor","group":"on","schedule_ts":1732060351,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"api_docs_simplify_tutorials":{"experiment_id":"7629258500165","type":"visitor","group":"on","schedule_ts":1729024584,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"contact_sales_dept_removal":{"experiment_id":"6538486873169","type":"visitor","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"salesforce_slack_integration":{"experiment_id":"7618340570659","type":"visitor","group":"on","schedule_ts":1727389057,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketing_ad_app_store_urls":{"experiment_id":"7746105288676","type":"visitor","group":"on","schedule_ts":1726699830,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"search_zd_vs_solr":{"experiment_id":"1355709002145","type":"visitor","group":"control","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"desktop_updater_v3_public_latest_release":{"experiment_id":"6724457596097","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"slack_developer_join_settings_rearch":{"experiment_id":"6917822477282","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"slack_developer_program":{"experiment_id":"5782848233798","type":"visitor","group":"on","schedule_ts":1709242483,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"downloads_s2p_promo":{"experiment_id":"7132023966439","type":"visitor","group":"treatment","trigger":"hash_visitor","schedule_ts":1718307458,"log_exposures":true,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"marketing_sc_rum_integration":{"experiment_id":"2491795733043","type":"visitor","group":"off","trigger":"hash_visitor","schedule_ts":1631738284,"log_exposures":true,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"paid_lp_expand":{"experiment_id":"7134287733637","type":"visitor","group":"treatment","schedule_ts":1717713269,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketing_live_chat_emea":{"experiment_id":"7226533858036","type":"visitor","group":"on","schedule_ts":1717629445,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"crypto_sidecar_for_comparable_keychains":{"experiment_id":"7041197731428","type":"visitor","group":"on","schedule_ts":1715184970,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"new_paid_lp":{"experiment_id":"6818768684695","type":"visitor","group":"treatment","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"slack_elevate_launch":{"experiment_id":"6966627699558","type":"visitor","group":"on","schedule_ts":1713959798,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketing_recaptcha_hc":{"experiment_id":"6963734115829","type":"visitor","group":"on","schedule_ts":1713301140,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketing_hc_flow_specifier":{"experiment_id":"6989238991504","type":"visitor","group":"on","schedule_ts":1713296815,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"anthony_test_visitor_1":{"experiment_id":"6823470010164","type":"visitor","group":"treatment","schedule_ts":1712613615,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketing_media_kit":{"experiment_id":"6696687337684","type":"visitor","group":"on","schedule_ts":1709232747,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"mris_usercreator_live":{"experiment_id":"4921780175444","type":"visitor","group":"on","schedule_ts":1706216435,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"out_of_office_xmas_jp":{"experiment_id":"6296845198293","type":"visitor","group":"off","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"out_of_office_xmas":{"experiment_id":"6322553087328","type":"visitor","group":"off","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"marketing_hreflang_errors_fix":{"experiment_id":"6319747700807","type":"visitor","group":"on","schedule_ts":1702931766,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"eg_pricing":{"experiment_id":"6266727458225","type":"visitor","group":"on","schedule_ts":1702587412,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"new_gated_demo":{"experiment_id":"6171698537921","type":"visitor","group":"on","schedule_ts":1701209093,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"marketing_cj":{"experiment_id":"5820701519667","type":"visitor","group":"on","schedule_ts":1699033035,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"deny_russian_ip":{"experiment_id":"3201051153989","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"swap_ukraine_logo_toggle":{"experiment_id":"5598910456034","type":"visitor","group":"on","schedule_ts":1689885040,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"customer_awards_launch":{"experiment_id":"2673548411155","type":"visitor","group":"on","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"},"slack_ie_address":{"experiment_id":"4857849748754","type":"visitor","group":"on","schedule_ts":1677793396,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"proj_brand_customer_stories_lp":{"experiment_id":"3448021380448","type":"visitor","group":"on","schedule_ts":1653596127,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"digital_first_lightning_strike_custacq":{"experiment_id":"2220660679364","type":"visitor","group":"on","schedule_ts":1625075563,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"cust_acq_partners_template":{"experiment_id":"2232204551504","type":"visitor","group":"treatment","schedule_ts":1628191410,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"community_launch":{"experiment_id":"2652841576373","type":"visitor","group":"on","schedule_ts":1635871147,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c","trigger":"launch_visitor","log_exposures":false},"app_directory_aws_promotion_banner":{"experiment_id":"3025397781073","type":"visitor","group":"control","trigger":"finished","log_exposures":false,"exposure_id":"0f96e9c22fe38078bb01a1f60e20317c"}},"no_login":false};</script><script type="text/javascript" crossorigin="anonymous" src="https://a.slack-edge.com/bv1-13/primer-vendor.8053ef7b3d5d7fad6d8b.primer.min.js" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null"></script><script type="text/javascript" crossorigin="anonymous" src="https://a.slack-edge.com/bv1-13/login-core.54390730bc75dd969cde.primer.min.js" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" data-critical></script><link href="https://a.slack-edge.com/bv1-13/login-core.28858849fa0fdabf58e7.primer.min.css" rel="stylesheet" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><link href="https://a.slack-edge.com/bv1-13/rollup-style-slack-kit-base.5dfb0f19d3a99d78a011.min.css" rel="stylesheet" id="slack_kit_helpers" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><link href="https://a.slack-edge.com/bv1-13/rollup-style-slack-kit-helpers.9c77b7d4b109618ba77b.min.css" rel="stylesheet" id="slack_kit_helpers" type="text/css" onload="window._cdn ? _cdn.ok(this, arguments) : null" onerror="window._cdn ? _cdn.failed(this, arguments) : null" crossorigin="anonymous"><script>if (window._cdn) _cdn.scanPageAssets();</script>

<!-- slack-www-hhvm-main-iad-wquj/ 2025-07-31 00:36:28/ vf1cdd0c1e6ff1f9d74b7158a8377f9008ea2e77e/ B:H -->

</body></html>