from .functions import *
from .config import *
import subprocess

class Notice:
    def __init__(self,path_file:str)->None:
        self.path_file=path_file
    def get_infos(self)->None:
        read_info_file(self,self.path_file,DIVISOR_VAR_CONTENT)
    def get_attribute(self,attr_name:str)->list:
        if not attr_name.upper() in self.__dict__.keys():
            print("Doesn't exist this attribute")
            return ''
        return self.__dict__[attr_name.upper()]
    #
    def display(self)->None:
        display_class_cli(self)

"""
tst=Notice("../database/notices/Pele_vivo.txt")
tst.get_infos()
tst.display()
"""
