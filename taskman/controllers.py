from flask import (
    Blueprint, redirect, render_template, request, url_for, abort
)

import components
import importlib
import os
from components.base_component import BaseComponent
import json

bp = Blueprint('taskman', __name__, url_prefix='/taskman')

@bp.route('/')
def index():
    data: dict = dict(
        name="John Doe",
        ip_address=f'1.1.1.1',
    )
    return render_template('hello.html', data=data)


@bp.route('/about', methods=('GET',))
def about():
    return "<p>About TASKMAN</p>"


@bp.route('/components')
def components():
    loaded = load_components()
    components_list = []
    #print(loaded)
    #print(loaded)
    #print(loaded.__dir__())
    for l in loaded:
        #print(l)
        #print(l.__dir__())
        components_list.append(l)
    return components_list



def load_components():
    # TODO: 
    # 1. return a serialized object 
    # 2. extract and return the needed information (TODO: decide what data is relevant for components)
    components = {}
    components_dir = "components"
    for filename in os.listdir(components_dir):
        if filename.endswith(".py") and filename != "base_component.py":
            module_name = filename[:-3]
            #print(module_name)
            #print(__package__)
            module = importlib.import_module(f".{module_name}", package="components")
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type) and issubclass(attribute, BaseComponent) and attribute != BaseComponent:
                    components[module_name] = attribute()
    return components