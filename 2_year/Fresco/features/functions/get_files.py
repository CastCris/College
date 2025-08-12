import subprocess
#
def get_files(dir_path:str,pattern:str)->list:
    files=subprocess.run(["find",dir_path,"-name",pattern],text=True,capture_output=True)
    files=files.stdout.strip().split('\n')
    #
    print(files)
