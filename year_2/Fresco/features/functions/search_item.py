import subprocess
#
def match_item(item:str,pattern:str)->int:
    pipe1 = subprocess.Popen(["echo",item],stdout=subprocess.PIPE) 
    pipe2 = subprocess.Popen(["grep","-E",pattern],stdin=pipe1.stdout,stdout=subprocess.PIPE) 
    pipe1.stdout.close()
    
    result,_ =pipe2.communicate() 
    result = result.decode().strip() 
    print(result)

    return len(result)

# print(match_item("comedia","ome"))
