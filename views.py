from flask import render_template, request, redirect, url_for, jsonify
from app import app
from ADmanage import *


module_functions = {
        'get_ADobjects': get_ADobjects,
        'get_ADobject': get_ADobject,
        'add_ADobject': add_ADobject,
        'del_ADobject': del_ADobject,
        'get_member': get_member,
        'get_memberOf': get_memberOf,
        'add_ADobject_to_group': add_ADobject_to_group,
        'del_ADobject_from_group': del_ADobject_from_group,
        'modify_ADobject_attributes': modify_ADobject_attributes,
        'reset_password': reset_password,
        'enable_ADobject': enable_ADobject,
        'disable_ADobject': disable_ADobject
    }


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html')

    module = request.form['module']
    arg1 = request.form['arg1']
    arg2 = request.form['arg2']
    selected_function = module_functions.get(module, None)

    if arg1 and arg2:
        results = str(selected_function(arg1, arg2))
    elif arg1 and not arg2:
        results = str(selected_function(arg1))
    else:
        results = list(selected_function())
    return render_template('index.html', results=results)
