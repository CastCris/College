import vlc
import time
import random
import subprocess

DIRECTORY_MUSIC="./musics"
MUSIC_FORMAT="*.mp3"
INFOS_FORMAT="infos.txt"

DIVISOR_VAR_NAME_CONTENT='='

YELLOW_COLOR='\033[1;33m'
NO_COLOR='\033[0m'
FILL_SYMBOL_CENTER='-'

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
            i=i.lower()
            if not DIVISOR_VAR_NAME_CONTENT in i:
                setattr(self,prev_name,prev_cont+'\n'+i)
                prev_cont=self.__dict__[prev_name]
                continue
            name_content=i.split(DIVISOR_VAR_NAME_CONTENT)
            setattr(self,name_content[0],name_content[1])

            prev_name=name_content[0]
            prev_cont=name_content[1]

    def display_infos(self)->None:
        terminal_width=int(subprocess.run(["tput","cols"],text=True,capture_output=True).stdout)
        half_terminal=terminal_width//2
        name=self.__dict__['name'].upper()

        print(FILL_SYMBOL_CENTER*half_terminal)
        print(YELLOW_COLOR+name+NO_COLOR)
        print(FILL_SYMBOL_CENTER*half_terminal)
        #
        for i in self.__dict__.keys():
            print('{} : {}'.format(i,self.__dict__[i]))
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
        media.parse_with_options(vlc.MediaParseFlag.local,timeout=5000)
        #
        time.sleep(1)
        self.player_duration=media.get_duration()
        #
        self.player=instance.media_player_new()
        self.player.set_media(media)
    def sound_play(self)->None:
        self.player.play()
    def sound_pause(self)->None:
        self.player.pause()
    def get_state(self)->object:
        return self.player.get_state()
    def get_time_pass(self)->int:
        return self.player.get_time()
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
    # Musics
    global musics
    # Sound manage
    global player
    # Order musics
    global order_musics
    ###
    # Musics
    musics=get_musics()
    # Sound manage
    player=Player()
    # Order musics
    order_musics=random.sample(musics,len(musics))

###

"""
player=Player()
for i in get_musics():
    i.get_infos()
    i.display_infos()
    #
    player.define_media(i.path_audio)
    player.sound_play()
    print(player.player_duration)
    while player.get_state() != vlc.State.Ended:
        print(player.get_time_pass())
        time.sleep(1)
"""
init_game_quiz()
for i in order_musics:
    i.get_infos()
    i.display_infos()
