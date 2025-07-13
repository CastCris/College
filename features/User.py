from .functions import *
from .config import *
import subprocess
#
class User(Generic_class_info):
    def __init__(self,path_infos)->None:
        self.path_infos=path_infos
        self.USER_NAME=path_infos.split('/')[-1]
        self.USER_NAME=self.USER_NAME.split('.')[0]

class User_Manager:
    def __init__(self,dir_control)->None:
        self.dir_control=dir_control
    def get_user(self,user_name)->object:
        user_file=subprocess.run(["find",self.dir_control,"-type","f","-name",user_name+'.txt'],text=True,capture_output=True)
        user_file=user_file.stdout.strip()
        if len(user_file.split('\n'))>1:
            print("This user is duplicate")
            return
        print(self.dir_control)
        user=User(user_file)
        user.get_infos()

        return user
