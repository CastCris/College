import os
import random
import subprocess
import playsound3

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
#
def get_files(dir_path:str,name_files:str)->str:
    files=subprocess.run(["find",dir_path,"-type","f","-name",name_files],text=True,capture_output=True)
    files=files.stdout
    files=files.split('\n')
    return files
def get_musics()->'list':
    audios=get_files(".","*.mp3") #get_files("./musics/audios/Skank","*.mp3")
    lyrics=get_files(".","*.txt") #get_files("./musics/lyrics/Skank","*.txt")
    #
    path_lyrics={}
    for i in lyrics:
        if not len(i):
            continue
        i,_=os.path.splitext(i)
        path_music=i.split('/')
        #
        sound_name=path_music[-1] # file
        artist=path_music[-2] # parent file
        #
        # print(sound_name)
        # print(artist)
        #
        key_name=artist+' - '+sound_name
        path_lyrics[key_name]=i
    #
    musics=[]
    for i in audios:
        if not len(i):
            continue
        i,_=os.path.splitext(i)
        path_music=i.split('/')
        #
        sound_name=path_music[-1]
        artist=path_music[-2]
        #
        key_name=artist+' - '+sound_name
        if not key_name in path_lyrics.keys():
            continue
        musics.append(Music(key_name,artist,i,path_lyrics[key_name]))
    return musics
###
def init_game_quiz()->None:
    # Head vars
    global musics
    global musics_by_artist
    # Question orders
    global order_artist
    # Able commands
    global commands
    # States
    global all_states
    global curr_state
    # Questions
    global type_question
    global curr_question
    global curr_sound
    ##
    # Head vars
    musics=get_musics()
    musics_by_artist={}
    for i in musics:
        if not i.author in musics_by_artist.keys():
            musics_by_artist[i.author]=[i.name]
            continue
        musics_by_artist[i.author].append(i.name)

    for i in musics_by_artist.keys():
        musics_by_artist[i]=random.sample(musics_by_artist[i],len(musics_by_artist[i]))
    # Questions orders
    order_artist=random.sample(list(musics_by_artist.keys()),len(list(musics_by_artist.keys())))
    # Able commands
    commands=["go","stop","try"]
    # States
    all_states=["listing","guest"]
    curr_state=""
    # Questions
    type_question={
            1:"From which band is this sound?",
            2:"Type a lyric {} sound",
            3:"Which band is the {} sound?",
            4:"Type the lyric of {} sound NOW!"
            }
    curr_question=""
    
def move_game_quiz(cmd:str)->None:
    cmd=cmd.split()
    if not cmd[0] in commands:
        print("Invalid command")
        return
    if 
        
if __name__=="__main__":
    init_game_quiz()
    for i in musics_by_artist.keys():
        print(musics_by_artist[i])
    print(order_artist)
