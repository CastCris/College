import vlc
import time
import random
import subprocess

COLOR_INFOS="\033[1;49;33m"
NO_COLOR="\033[0m"

class Music:
    def __init__(self,name:str,author:str,path_audio:str,path_lyric:str)->None:
        self.name=name
        self.author=author
        self.path_audio=path_audio
        self.path_lyric=path_lyric
        # self.duration
    def play_sound(self):
        pass
    #
    def display_infos(self):
        music_name_size=len(self.name)
        console_size=int(subprocess.run(["tput","cols"],text=True,capture_output=True).stdout)

        size_bars=console_size//2-music_name_size//2
        one_plus_minus=1 if size_bars*2+music_name_size<console_size else -1 if size_bars*2+music_name_size>console_size else 0
        #
        print(size_bars)
        print("-"*(size_bars+one_plus_minus),end='')
        print(COLOR_INFOS+self.name+NO_COLOR,end='')
        print("-"*(size_bars),end='')
        #
        print(f"author = {self.author:>10}\npath audio =  {self.path_audio}\npath lyrics = {self.path_lyric:>10}")

def get_media(media_path:str)->None:
    global player
    global player_media_time
    #
    instance_media=vlc.Instance()
    #
    media=instance_media.media_new(media_path)
    media.parse_with_options(vlc.MediaParseFlag.local, timeout=5000)
    #
    time.sleep(1)
    duration_ms=media.get_duration()
    ##
    player=instance_media.media_player_new()
    player.set_media(media)
    player_media_time=duration_ms
    print(player_media_time)

    player.play()
def get_player_time()->int:
    curr_time=player.get_time()
    return curr_time
def sound_play():
    player.play()
def sound_pause():
    player.pause()
def decision_player(cmd:str,media_path:str)->None:
    if not player or player.get_state()==vlc.State.Ended:
        get_media('./musics/Skank/Acima_do_Sol/Acima_do_Sol.mp3')
    if cmd=="stop":
        sound_pause()
        return
    sound_play()
##
def init_game_quiz()->None:
    # Sound manage
    global player
    global player_media_time
    ###
    player_state=None
    player=None

while True:
    inp=input('*: ')
    decision_player(inp)

