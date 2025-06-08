from core import AppModule

from blogs import BlogModule
from admin import AdminModule
from web_page import WebPageModule
from taskman import TaskmanModule


APP_MODULES: set[AppModule] = {
    BlogModule(),
    AdminModule(),
    WebPageModule(),
    TaskmanModule()
}