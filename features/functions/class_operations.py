import subprocess
from ..config import *
#
def read_info_file(class_obj:object,path_infos:str,divisor:str)->None:
    with open(path_infos,'r') as file:
        content_file=file.read().strip().split('\n')
        var_name=''
        for i in content_file:
            splited_i=i.strip().split(divisor)
            #
            if len(splited_i)==1 and len(var_name):
                class_obj.__dict__[var_name].append(splited_i[0])
                continue
            if len(splited_i)==1 and not len(var_name):
                continue

            var_name=splited_i[0].upper()
            var_content=splited_i[1]
            setattr(class_obj,var_name,[var_content])
def display_class_cli(class_obj:object)->None:
    console_width=subprocess.run(["tput","cols"],text=True,capture_output=True)
    console_width=int(console_width.stdout.strip())
    tabulation_len=0
    for i in class_obj.__dict__.keys():
        if len(i)>tabulation_len:
            tabulation_len=len(i)
    #
    print('='*console_width)
    for i in class_obj.__dict__.keys():
        print(f"{GREEN_COLOR}{i:<{tabulation_len}} = {NO_COLOR}{class_obj.__dict__[i]}")
    print('='*console_width)
