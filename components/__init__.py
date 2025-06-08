from core import AppModule
import importlib
import os
from components import base_component

def load_components():
    components = {}
    components_dir = os.path.dirname(__file__)
    for filename in os.listdir(components_dir):
        if filename.endswith(".py") and filename != "base_component.py":
            module_name = filename[:-3]
            module = importlib.import_module(f".{module_name}", package=__package__)
            for attribute_name in dir(module):
                attribute = getattr(module, attribute_name)
                if isinstance(attribute, type) and isubclass(attribute, BaseComponent) and attribute != BaseComponent:
                    components[module_name] = attribute()
    return components