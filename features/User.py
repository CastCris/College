from .General_classes import *
from .functions import *
from .config import *
import subprocess
#
class User(Generic_class_info):
    def __init__(self,path_infos)->None:
        self.path_infos=path_infos
        self.USER_NAME=path_infos.split('/')[-1]
        self.USER_NAME=self.USER_NAME.split('.')[0]

class User_Manager(Generic_manager):
    def get_user(self,user_name:str)->object:
        user_file=self.get_item(user_name)
        if len(user_file)>2:
            print(RED_COLOR+f"The {user_name} user is duplicate"+NO_COLOR)
            return
        if not len(user_file):
            print(RED_COLOR+f"The {user_name} doesn't exist"+NO_COLOR)
            return
        return User(user_file[0])
