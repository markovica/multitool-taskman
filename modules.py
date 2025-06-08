from core import AppModule

from blogs import BlogModule
from admin import AdminModule
from web_page import WebPageModule
from taskman import TaskmanModule
#from components import load_components


APP_MODULES: set[AppModule] = {
    BlogModule(),
    AdminModule(),
    WebPageModule(),
    TaskmanModule(),
    
}