from core import AppModule
from taskman import controllers


class TaskmanModule(AppModule):

    def __init__(self):
        self.blueprint = controllers.bp
        self.template_folder = 'taskman/templates'
        self.permission_names = set()
        super().__init__('taskman')