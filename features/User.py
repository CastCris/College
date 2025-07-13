from .functions import *
from .config import *
import subprocess
#
class User:
    def __init__(self,path_infos:str)->None:
        self.path_infos=path_infos
    def get_infos()->None:
        read_info_file(self,self.path_infos)
    def display()->None:
        display_class_cli(self)

class User_Manager:
    def __init__(self,dir_control)->None:
        self.dir_control=dir_control
    def get_user(self,user_name)->None:
        user_file=subprocess.run(["find",self.dir_control,"-type","f","-name",user_name],text=True,capture_output=True)
        user_file=user_file.stdout.strip()
        if len(user_file.split('\n'))>1:
            print("This user is duplicate")
            return

