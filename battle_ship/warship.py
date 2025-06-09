import random
import subprocess

PREFIXES_WARSHIPS = [
    "USS",
    "HMS",
    "INS",
    "JS", 
    "KRI",
    "HMAS"
    "FS", 
    "BNS",
    "ARC",
    "BRP",
    "NRP",
    "HTMS"
    "ROKS"
    "TNS",
    "AOR",
]
SUFFIXES_WARSHIPS = [
    "Thunderbolt",
    "Vikrant",
    "Yamato",
    "Dreadnought",
    "Sachsen",
    "Arleigh Burke",
    "Charles de Gaulle",
    "Independence",
    "Zumwalt",
    "Triumph",
    "Varyag",
    "São Paulo",
    "Kaga",
    "Formidable",
    "Tarlac",
]
SYMBOLS_SMALL  = [chr(i+97) for i in range(26)]
SYMBOLS_MEDIUM = [chr(i+48) for i in range(10)]
SYMBOLS_BIG    = [chr(i+33) for i in range(10) if chr(i+33) != '(' and chr(i+33) != ')' and chr(i+33) != '\'']

SMALL=3
MEDIUM=7

###
def generate_warships_names(amount_ships:int,already_used_names:'list')->'list':
    warships_names=[]
    prefixe=PREFIXES_WARSHIPS[int(random.random()*len(PREFIXES_WARSHIPS))]
    for _ in range(amount_ships):
        suffixe=SUFFIXES_WARSHIPS[int(random.random()*len(SUFFIXES_WARSHIPS))]
        name=prefixe+' '+suffixe
        
        loops=0
        while True:
            temp=name+'-'+str(loops)
            if not temp in warships_names and not temp in already_used_names:
                name=temp
                break
            loops+=1
        warships_names.append(name)
    return warships_names
def generate_table(height:int,width:int)->'list':
    table=[[0 for _ in range(width)] for _ in range(height)]
    return table
def display_table(table:'list',size_each_name:'dict')->None:
    link_name_symbol={}
    index_small=0
    index_medium=0
    index_big=0
    for i in size_each_name.keys():
        if size_each_name[i] <= SMALL:
            link_name_symbol[i]=SYMBOLS_SMALL[index_small]
            index_small+=1
        elif size_each_name[i] <= MEDIUM:
            link_name_symbol[i]=SYMBOLS_MEDIUM[index_medium]
            index_medium+=1
        else:
            link_name_symbol[i]=SYMBOLS_BIG[index_big]
            index_big+=1

        index_small%=len(SYMBOLS_SMALL)
        index_medium%=len(SYMBOLS_MEDIUM)
        index_big%=len(SYMBOLS_BIG)

    longest_str=0
    for i in table:
        for j in i:
            if not j:
                print('.',end=' ')
            elif j == 1:
                print('X',end=' ')
            else:
                print(link_name_symbol[j],end=' ')
            if len(str(j)) > longest_str:
                longest_str=len(str(j))
        print()
    longest_str+=2
    print('Caption:')
    for i in link_name_symbol.keys():
        print(f"{i:<{longest_str}} = {link_name_symbol[i]}")
#
def check_able_lines(table:'matrix',ship_size:int)->'list':
    table_height=len(table)
    table_width=len(table[0])
    #
    able_columns=[[0 for i in range(table_width)] for j in range(table_height)]
    tag_columns=[[] for i in range(table_height)]
    for i in range(table_height):
        tag_columns[i].append(-1)
        for j in range(table_width):
            if table[i][j]:
                tag_columns[i].append(j)
        tag_columns[i].append(table_width)

    """
    for i in tag_columns:
        print(i)
    print()
    """

    for i in range(table_height):
        index=0
        index1_tag,index2_tag=0,1
        while index<table_width:
            if index==tag_columns[i][index2_tag]:
                index1_tag+=1
                index2_tag+=1
                index+=1
                continue
            #
            if tag_columns[i][index2_tag]-index>=ship_size: # forward
                able_columns[i][index]+=1
            if index-tag_columns[i][index1_tag]>=ship_size: # backward
                able_columns[i][index]+=2
            index+=1

    """
    for i in able_columns:
        print(i)
    """
    return able_columns
def check_able_columns(table:'matrix',ship_size:int)->'list':
    table_height=len(table)
    table_width=len(table[0])
    table_rev=[[] for i in range(table_width)]

    for i in range(table_width):
        for j in range(table_height):
            table_rev[i].append(table[j][i])

    """
    for i in table_rev:
        print(i)
    """
    return check_able_lines(table_rev,ship_size)
#
def put_randomly_ships_in_table(ships:'list',table:'matrix',ships_names:'liat')->'dict':
    if not len(table):
        print('Empty table')
        return
    table_height=len(table)
    table_width=len(table[0])

    ships_fit=[]
    ships_fit_name=[]
    for i in range(len(ships)):
        if ships[i]>table_width and ships[i]>table_height:
            continue
        ships_fit.append(ships[i])
        ships_fit_name.append(ships_names[i])
    #
    ships_fit.sort()
    used_names={}
    for index in range(len(ships_fit)):
        i=ships_fit[index]
        ship_name=ships_fit_name[index]
        #
        able_columns,able_lines=[],[]
        able_columns=check_able_columns(table,i)
        able_lines=check_able_lines(table,i)
        ##
        spots_ships_lines=[]
        spots_ships_columns=[]
        for j in range(table_height):
            for k in range(table_width):
                if able_lines[j][k]:
                    spots_ships_lines.append(j)
                    break
        for j in range(table_width):
            for k in range(table_height):
                if able_columns[j][k]:
                    spots_ships_columns.append(j)
                    break
        if not len(spots_ships_lines) and not len(spots_ships_columns):
            continue
        #
        vertical=int(random.random()*2)
        if vertical and not len(spots_ships_columns):
            vertical=0
        elif not vertical and not len(spots_ships_lines):
            vertical=1
        #
        list_spots=[]
        chosen_list_spots=0
        if vertical:
            chosen_list_spots=spots_ships_columns[int(random.random()*len(spots_ships_columns))]
            list_spots=able_columns[chosen_list_spots]
        else:
            chosen_list_spots=spots_ships_lines[int(random.random()*len(spots_ships_lines))]
            list_spots=able_lines[chosen_list_spots]

        # print(vertical,list_spots)
        index_spots=[]
        for j in range(len(list_spots)):
            if list_spots[j]!=0:
               index_spots.append(j)
        ##
        print(list_spots,index_spots)
        line,column=None,None
        chosen_index=index_spots[int(random.random()*len(index_spots))]
        chosen=list_spots[chosen_index]
        print(chosen_index,chosen)
        if vertical:
            column=chosen_list_spots
            line=chosen_index
        else:
            line=chosen_list_spots
            column=chosen_index
        #
        direction=0 # 1:forward 2:backward
        if chosen<3:
            direction=chosen
        else:
            direction=int(random.random()*2+1)
        #
        print(vertical,direction)
        if vertical and direction==1:
            for j in range(i):
                table[line+j][column]=ship_name
        elif vertical and direction==2:
            for j in range(i):
                table[line-j][column]=ship_name

        if not vertical and direction==1:
            for j in range(i):
                table[line][column+j]=ship_name
        elif not vertical and direction==2:
            for j in range(i):
                table[line][column-j]=ship_name
        #
        print("Ship {} size: {}, line:{}, column:{}, direction: {}".format(ship_name,i,line,column,direction))
        used_names[ship_name]=i
    return used_names
###
def init_game_battleship(table_width:int,table_height:int,ships_list:"list")->None:
    global table_ship_user
    global table_ship_bot
    
    global table_shot_user
    global table_shot_bot

    global target_hit_user
    global target_hit_bot

    global puted_ships_user
    global max_ships

    global commands

    global ships
    global total_blocks
    ## Init vars
    table=[[0 for i in range(table_width)] for j in range(table_height)]
    table_ship_user=table.copy()
    table_ship_bot=table.copy()

    table_shot_user=table_ship_user.copy()
    table_shot_bot=table_ship_bot.copy()

    target_hit_user=0
    target_hit_bot=0

    puted_ships_user=0
    max_ships=len(ships_list)
    #
    commands=["s","p"] # shot,put
    #
    ships=ships_list
    total_blocks=0
    for i in ships:
        total_blocks+=i
def move_game_battleship(cmd:str)->None:
    cmd=cmd.split()
    if not cmd[0] in commands:
        print("Invalid command")
        return -1
    if cmd[0]=="p":
        put_ships_table(cmd[1:])
        return 0
    if puted_ships!=max_ship:
        print("Please, put all ships in table!")
        return 0
###

if __name__=='__main__':
    table=[
            [0,1,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [0,0,0,0,0,1,1],
            [0,0,1,0,0,0,0]
            ]
    table=[
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
            ]
    table=generate_table(10,5)
    #check_able_lines([],table,4)
    #check_able_columns([],table,2)
    names=generate_warships_names(25,[])
    names=put_randomly_ships_in_table([4,3,2,1,3,10],table,names)
    display_table(table,names)
