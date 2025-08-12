import random

def check_play()->int:
    global user_option
    global comp_option

    comp_option=int(random.random()*3)
    user_option=translate[user_option]
    # print(str(user_option)+" X "+str(comp_option))
    print("Computer choose: ",end='')
    if not comp_option:
        print("Rock")
    elif comp_option==1:
        print("Paper")
    else:
        print("Scissors")
    #
    if combinations[user_option+1]==comp_option:
        return 0
    if combinations[user_option-1]==comp_option:
        return 2
    return 1
#
def init_game_jokenpo()->None:
    global combinations
    global translate

    global user_option
    global comp_option
    global cmd_option

    global user_score
    global bot_score
    #
    combinations=[2,0,1,2,0] # 0:Rock 1:Paper 2:scissors
    translate={
            'R':1,
            'P':2,
            'S':3
        }

    user_option=-1
    comp_option=-1
    cmd_option=["p","s"]

    user_score=0
    bot_score=0

def move_game_jokenpo(cmd:str)->None:
    global user_option
    global user_score
    global bot_score

    cmd=cmd.split()
    if not cmd[0] in cmd_option:
        print("Invalid command")
        return -1
    if cmd[0]=="p":
        user_option=cmd[1]
        res=check_play()
    if cmd[0]=="s":
        print("User score: {} \t Computer Score: {}".format(user_score,bot_score))
        return 0
    #
    if not res:
        print("You lost!")
        bot_score+=1
        return 0
    if res==1:
        print("Tie")
        return 0
    if res==2:
        print("You win!")
        user_score+=1
        return 0

    print(res)

def finish_game_jokenpo()->None:
    global combinations
    global translate

    global user_option
    global comp_option
    global cmd_option

    global user_score
    global bot_score
    ###
    del combinations
    del translate

    del user_option
    del comp_option
    del cmd_option

    del user_score
    del bot_score

###
""" COMMANDS
p [R,P,S]   -> Play, select R(rock), P(papaer) and S(scissor)
s           -> See the score
"""
if __name__=="__main__":
    while True:
        init_game_jokenpo()
        while True:
            inp=input('*: ')
            move_game_jokenpo(inp)
        finish_game_jokenpo()
