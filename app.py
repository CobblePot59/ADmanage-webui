from flask import Flask
from flask_toastr import Toastr
from ADmanage import ADclient

app = Flask(__name__)
app.config.from_pyfile('config.py')

toastr = Toastr(app)

ad_client = ADclient(domain=app.config['LDAP_DOMAIN'], username=app.config['LDAP_USERNAME'], password=app.config['LDAP_PASSWORD'], dc_ip=app.config['LDAP_HOST'], base_dn=app.config['LDAP_BASE_DN'], secure=app.config['LDAPS'])

from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
