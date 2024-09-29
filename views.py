from flask import render_template, request
from app import app, ad_client
import json

module_functions = {
        'get_DNSentries': ad_client.get_DNSentries,
        'get_DNSentry': ad_client.get_DNSentry,
        'add_DNSentry': ad_client.add_DNSentry,
        'modify_DNSentry': ad_client.modify_DNSentry,
        'del_DNSentry': ad_client.del_DNSentry,
        'get_ADobjects': ad_client.get_ADobjects,
        'get_ADobject': ad_client.get_ADobject,
        'add_ADobject': ad_client.add_ADobject,
        'del_ADobject': ad_client.del_ADobject,
        'get_member': ad_client.get_member,
        'get_memberOf': ad_client.get_memberOf,
        'add_ADobject_to_group': ad_client.add_ADobject_to_group,
        'del_ADobject_from_group': ad_client.del_ADobject_from_group,
        'modify_ADobject_attributes': ad_client.modify_ADobject_attributes,
        'reset_password': ad_client.reset_password,
        'enable_ADobject': ad_client.enable_ADobject,
        'disable_ADobject': ad_client.disable_ADobject
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html', module_functions=list(module_functions.keys()))

    module = request.form.get('module')
    arg1 = request.form.get('arg1')
    arg2 = request.form.get('arg2')
    selected_function = module_functions.get(module, None)

    if arg1 and arg2:
        results = json.dumps(selected_function(arg1, arg2), indent=4)
    elif arg1 and not arg2:
        results = json.dumps(selected_function(arg1), indent=4)
    else:
        results = json.dumps(selected_function(), indent=4)
    return render_template('index.html', module_functions=list(module_functions.keys()), results=results)
