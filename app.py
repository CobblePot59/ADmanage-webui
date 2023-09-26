from flask import Flask
from ldap3 import Server, Connection, ALL
from flask_toastr import Toastr

app = Flask(__name__)
app.config.from_pyfile('config.py')

toastr = Toastr(app)

sam = f"{app.config['LDAP_USERNAME']}@{app.config['LDAP_DOMAIN']}"
dc_url = f"{app.config['LDAP_SCHEMA']}://{app.config['LDAP_HOST']}:{app.config['LDAP_PORT']}"
base_dn = app.config['LDAP_BASE_DN']
server = Server(dc_url, get_info=ALL)
conn = Connection(server, user=sam, password=app.config['LDAP_PASSWORD'], auto_bind=app.config['LDAP_BIND_DIRECT_CREDENTIALS'])

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
