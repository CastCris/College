import os
import subprocess
from ..config import *
#
def get_attr_from_str(attr:str,divisor:str)->dict:
    item_attr={}
    var_name=''
    for i in attr.split('\n'):
        splited_i=i.split(divisor)
        if len(splited_i)==1 and len(var_name):
            item_attr[var_name].append(splited_i)
            continue
        if len(splited_i)==1 and not len(var_name):
            continue
        var_name=splited_i[0].upper()
        var_cont=splited_i[1]
        item_attr[var_name]=[var_cont]
    return item_attr
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
    def update_attr(self,attr_name:str,new_content:str)->None:
        if not attr_name in self.__dict__:
            print(RED_COLOR+"Thus attribute doesn't exist in this class"+NO_COLOR)
        self.__dict__[attr_name]=new_content
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
        if not os.path.exists(path_control):
            print(RED_COLOR+"This path doesn't exist"+NO_COLOR)
        self.path_control=path_control
    def get_item(self,item_name:str)->list:
        items=subprocess.run(["find",self.path_control,"-type","f","-name",item_name+TYPE_FILE_INFOS],text=True,capture_output=True)
        items=items.stdout.strip().split('\n')
        if not len(items[0]):
            print(RED_COLOR+"This item doesn't exist"+NO_COLOR)
            return []
        return items
    def create_item(self,item_name:str,item_cont:dict,divisor:str)->None:
        subprocess.run(["touch",self.path_control+'/'+item_name+TYPE_FILE_INFOS])
        with open(self.path_control+'/'+item_name+TYPE_FILE_INFOS,'w') as file:
            for i in item_cont.keys():
                line=i+divisor+'\n'.join(item_cont[i])+'\n'
                file.write(str(line))
    def delete_item(self,item_name:str)->None:
        if not len(self.get_item(item_name)):
            return
        os.remove(self.path_control+'/'+item_name+TYPE_FILE_INFOS)
    def update_item(self,item_name:str,item_attr:str,item_attr_new:str,divisor:str)->None:
        if not len(self.get_item(item_name)):
            return
        item_attr=item_attr.upper()
        with open(self.path_control+'/'+item_name+TYPE_FILE_INFOS,'r') as file:
            print(file)
            item=get_attr_from_str(file.read().strip(),divisor)
            if not item_attr in item.keys():
                print(RED_COLOR+f"The attribute {item_attr} doesn't exist in class"+NO_COLOR)
                return
            item[item_attr]=[item_attr_new]
            #
            self.create_item(item_name,item,divisor)
