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
def get_music_from_list(set_musics:'list',name:str,band:str)->object:
    for i in set_musics:
        if i.name==name and i.author==band:
            return i
    return None
###
def init_game_quiz()->None:
    # Head vars
    global musics
    global musics_by_artist
    # Question orders
    global order_artist
    global order_musics_by_artist
    # Able commands
    global commands
    # States
    global all_states
    global curr_state
    # Questions
    global type_question
    global curr_question
    global curr_artist
    global curr_sound

    global answer
    # Score
    global global_score
    global potential_score
    ##
    # Head vars
    musics=get_musics()
    musics_by_artist={}
    for i in musics:
        if not i.author in musics_by_artist.keys():
            musics_by_artist[i.author]=[i.name]
            continue
        musics_by_artist[i.author].append(i.name)

    # Questions orders
    order_artist=random.sample(list(musics_by_artist.keys()),len(list(musics_by_artist.keys())))
    order_musics_by_artist={}
    for i in order_artist:
        order_musics_by_artist[i]=random.sample(musics_by_artist[i],len(musics_by_artist[i]))
    # Able commands
    commands=["go","stop","try"]
    # States
    all_states=[0,1,2] # 0:listing, 1:stop_music, 2:guess
    curr_state=""
    # Questions
    type_question={
            0:"From which band is this sound?",
            1:"Type a passage of the {} sound",
            2:"Which band is the {} sound?",
            3:"Type the lyric of {} sound NOW!",
            4:"What is the name of this sound?"
            }
    curr_question=-1
    
    curr_artist=""
    curr_sound=""
    answer=""
    # Score
    global_score=0
    potential_score=0
    
def move_game_quiz(cmd:str)->None:
    cmd=cmd.split()
    #
    if not curr_state: # listing
        curr_state=1
        play
    #
    if not cmd[0] in commands:
        print("Invalid command")
        return
    #
    if cmd[0]=="go" and curr_question!=-1:
        print("You already have a question, answer it first!")
        return
    if cmd[0]=="go" and curr_question==-1:
        next_question()
        return
###
def next_question()->None:
    global curr_question
    global curr_artist
    global curr_sound
    global curr_state
    global answer
    #
    keys_type_question=list(type_question.keys())
    keys_type_question.pop(0)
    if not curr_artist in order_musics_by_artist.keys() or not len(order_musics_by_artist[curr_artist]):
        curr_question=0
        curr_artist=order_artist.pop(0)
    else:
        curr_question=random.sample(keys_type_question,len(keys_type_question))[int(random.random()*len(keys_type_question))]
    #
    curr_state="listing"
    sound_name=order_musics_by_artist[curr_artist].pop(0)
    curr_sound=get_music_from_list(musics,sound_name,curr_artist)
    print(curr_sound)
    #
    if not curr_question or curr_question==2:
        answer=curr_artist
        return
    if curr_question==1 or curr_question==3:
        answer=subprocess.run(["cat",curr_sound.path_lyric],text=True,capture_output=True)
        return 
    if curr_question==4:
        answer=curr_sound.name
        return
def ask_question()->None:
    question=type_question[curr_question]
    complement=""
    if curr_question in [1,2,3]:
        complement=curr_sound.name

    print(question.format(complement))

if __name__=="__main__":
    while True:
        init_game_quiz()
        while True:
            inp=input('*: ')
            move_game_quiz(inp)
            curr_sound.display_infos()
