import os
import random
import subprocess

COLOR_INFOS="\033[1;49;33m"
NO_COLOR="\033[0m"

class Music:
    def __init__(self,name:str,path_audio:str,path_lyric:str)->None:
        self.name=name
        self.path_audio=path_audio
        self.path_lyric=path_lyric
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
        print(f"Name = {self.name:>20}")

#
def get_files(dir_path:str,name_files:str)->str:
    files=subprocess.run(["find",dir_path,"-type","f","-name",name_files],text=True,capture_output=True)
    files=files.stdout
    files=files.split('\n')
    return files
def get_musics()->'list':
    audios=get_files(".","*.mp3")
    lyrics=get_files(".","*.txt")
    #
    path_lyrics={}
    for i in lyrics:
        sound_name=(i.split('/'))[-1]
        sound_name,_=os.path.splitext(sound_name)
        sound_name=sound_name.strip()
        print(sound_name)
        path_lyrics[sound_name]=i
    #
    musics=[]
    for i in audios:
        sound_name=(i.split('/'))[-1]
        sound_name,_=os.path.splitext(sound_name)
        sound_name=sound_name.strip()
        print(sound_name)
        if sound_name in path_lyrics.keys():
            musics.append(Music(sound_name,i,path_lyrics[sound_name]))
    return musics

# def init_game_quiz()->None:
#     global musics
    
if __name__=="__main__":
    tst=get_musics()
    for i in tst:
        i.display_infos()
