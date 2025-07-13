import os
import subprocess
from ..config import *
#
class Generic_class_info():
    def __init__(self,path_infos:str)->None:
        self.path_infos=path_infos
    def get_attr(self,attr_name)->list:
        if not attr_name in self.__dict__.keys():
            print("This attribute doesn't exist in this class")
            return
        return self.__dict__[attr_name]
    def get_infos(self,divisor)->None:
        with open(self.path_infos,'r') as file:
            content_file=file.read().strip().split('\n')
            var_name=''
            for i in content_file:
                splited_i=i.strip().split(divisor)
                #
                if len(splited_i)==1 and len(var_name):
                    self.__dict__[var_name].append(splited_i[0])
                    continue
                if len(splited_i)==1 and not len(var_name):
                    continue

                var_name=splited_i[0].upper()
                var_content=splited_i[1]
                setattr(self,var_name,[var_content])
    def display_cli(self)->None:
        console_width=subprocess.run(["tput","cols"],text=True,capture_output=True)
        console_width=int(console_width.stdout.strip())
        tabulation_len=0
        for i in self.__dict__.keys():
            if len(i)>tabulation_len:
                tabulation_len=len(i)
        #
        print('='*console_width)
        for i in self.__dict__.keys():
            print(f"{GREEN_COLOR}{i:<{tabulation_len}} = {NO_COLOR}{self.__dict__[i]}")
        print('='*console_width)
class Generic_manager():
    def __init__(self,path_control:str)->None:
        self.path_control=path_control
    def get_item(self,item_name:str)->list:
        items=subprocess.run(["find",self.path_control,"-type","f","-name",item_name],text=True,capture_output=True)
        items=items.stdout.strip().split('\n')
        return items
    def create_item(self,item_name:str,item_cont:dict,divisor:str)->None:
        with open(self.path_control+'/'+item_name) as file:
            for i in item_cont.keys():
                file.write(i+divisor+'\n'.join(item_cont[i]))
    def from_str_to_item(self,item_name:str,attr:str,divisor:str)->None:
        item_attr={}
        var_name=''
        for i in attr:
            splited_i=i.split(divisor)
            if len(splited_i)==1 and len(var_name):
                item_attr[var_name].append(splited_i)
                continue
            if len(splited_i)==1 and not len(var_name):
                continue
            var_name=splited_i[0]
            var_cont=splited_i[1]
            item_attr[var_name]=[var_cont]
        self.create_item(item_name,item_attr,divisor)
    def delete_item(self,item_name)->None:
        os.remove(self.path_item+item_name)
    def update_item(self,item_name,item_attr,item_attr_new,divisor)->None:
        item=self.get_item(item_name)
        item.get_infos(divisor)
        item[item_attr]=item_attr_new
        #
        self.delete_item(item_name)
        self.create_item(item_name,item.__dict__,divisor)
