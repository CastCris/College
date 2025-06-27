import vlc
import time
import random
import subprocess

DIRECTORY_MUSIC="./musics"
MUSIC_FORMAT="*.mp3"
INFOS_FORMAT="infos.txt"

DIVISOR_VAR_NAME_CONTENT='='

class Music:
    def __init__(self,path_audio:str,path_infos:str)->None:
        self.path_audio=path_audio
        self.path_infos=path_infos
    def get_infos(self)->None:
        file=open(self.path_infos,'r')
        prev_name=''
        prev_cont=''
        #
        cont_file=file.read().split('\n')
        for i in cont_file:
            if not len(i):
                continue
            if not DIVISOR_VAR_NAME_CONTENT in i:
                setattr(self,prev_name,prev_cont+'\n'+i)
                prev_cont=self.__dict__[prev_name]
                continue
            name_content=i.split(DIVISOR_VAR_NAME_CONTENT)
            setattr(self,name_content[0],name_content[1])

            prev_name=name_content[0]
            prev_cont=name_content[1]

    def display_infos(self)->None:
        print(self.__dict__)
class Player:
    def __init__(self)->None:
        self.media_path=None
        self.player=None
        self.player_duration=None
    def define_media(self,media_path:str)->None:
        self.media_path=media_path
        instance=vlc.Instance()
        #
        media=instance.media_new(self.media_path)
        media.parse_with_option(vlc.MediaParseFlag.local,timeout=5000)
        #
        time.sleep(1)
        self.player_duration=media.get_duration()
        #
        player=instance.media_player_new()
        player.set_media(media)
    def sound_play(self)->None:
        player.play()
    def sound_pause(self)->None:
        player.pause()
###
def get_files(path_dir:str,pattern:str)->'list':
    cmd_find=subprocess.run(["find",path_dir,"-name",pattern],text=True,capture_output=True)
    files=cmd_find.stdout.split('\n')
    return files
def get_musics()->'list':
    musics=[]
    path_infos=get_files(DIRECTORY_MUSIC,INFOS_FORMAT)
    path_audios=get_files(DIRECTORY_MUSIC,MUSIC_FORMAT)
    #
    able_audios={}
    for i in path_audios:
        if not len(i):
            continue
        cmd_dirname=subprocess.run(["dirname",i],text=True,capture_output=True)
        parent_dir=cmd_dirname.stdout
        able_audios[parent_dir]=i
    
    for i in path_infos:
        if not len(i):
            continue
        cmd_dirname=subprocess.run(["dirname",i],text=True,capture_output=True)
        parent_dir=cmd_dirname.stdout
        if parent_dir in able_audios.keys():
            musics.append(Music(able_audios[parent_dir],i))

    return musics

def init_game_quiz()->None:
    # Sound manage
    global player
    global player_media_time
    ###
    player_state=None
    player=None

###

for i in get_musics():
    i.get_infos()
    i.display_infos()
