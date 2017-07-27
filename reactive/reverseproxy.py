from charms.reactive import when, when_all, when_not, set_state
from charmhelpers.core import hookenv

import socket

@when_not('reverseproxy-charm.installed')
@when('layer-hostname.installed')
def install_reverseproxy():
    hookenv.status_set('maintenance','ready to configure')
    set_state('reverseproxy-charm.installed')

@when_all('reverseproxy.triggered','reverseproxy.ready','reverseproxy-charm.installed')
@when_not('reverseproxy.configured','reverseproxy.departed')
def configure_reverseproxy(reverseproxy,*args):
    # TODO: retrigger if config change?
    charm_config = hookenv.config()
    hookenv.log("Setting up reverseproxy", "INFO")
    proxy_info = {'mode':charm_config['mode'],
                  'urlbase':charm_config['urlbase'],
                  'subdomain':charm_config['subdomain'],
                  'group_id':charm_config['group-id'],
                  'external_port': charm_config['external-port'],
                  'internal_host': socket.getfqdn(),
                  'internal_port': charm_config['internal-port']
                  } 
    reverseproxy.configure(proxy_info)
    hookenv.status_set('active','')

#@when_all('reverseproxy.triggered','reverseproxy.departed')
#def remove_urlbase(reverseproxy,*args):
#    hookenv.log("Removing reverseproxy configuration", "INFO")

