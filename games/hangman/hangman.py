import subprocess
import random

def get_file()->"file":
    pwd=subprocess.run(["pwd"],text=True,capture_output=True)
    pwd=pwd.stdout
    dir_home=""
    for i in pwd.split('/'):
        dir_home+='/'+i
        if i=="home":
            break
    pipe1=subprocess.Popen(["find",dir_home,"-type","f"],stdout=subprocess.PIPE)
    pipe2=subprocess.Popen(["grep","-Eo",'.*\\.py$|.*\\.txt$'],stdin=pipe1.stdout,stdout=subprocess.PIPE)
    pipe1.stdout.close()

    dirs,_=pipe2.communicate()
    dirs=dirs.decode().strip()
    dirs=dirs.split()
    #
    file=None
    #
    while True:
        random_number=int(random.random()*len(dirs))
        select_dir=dirs[random_number]
        cat_file=subprocess.run(["cat",select_dir],capture_output=True,text=True)
        cat_file=cat_file.stdout
        if not len(cat_file):
            continue
        # print(select_dir)
        file=open(select_dir,'r')
        break
    return file

def count_lines(file:"file")->int:
    tot=0
    for line in file:
        # print(line)
        tot+=1
    file.seek(0)
    return tot

def get_random_phrase(file:"File")->str:
    random_num=int(random.random()*count_lines(file))
    index=0
    line=None
    for i in file:
        line=i
        if index>=random_num and len(line.strip()):
            break
        index+=1
    return line.strip()

def guess_word_hangman(letters:str)->int:
	global chances
	global errors
	global phrase
	global guested_phrase
	global no_chars
	global completed_chars
	#
	right_letters=[]
	for i in letters:
		if i in phrase and not i in right_letters and not i in guested_phrase:
			right_letters.append(i)
		elif not i in phrase:
			errors+=1
			no_chars.append(i)
	#
	new_guested=[]
	index=0
	while index<len(phrase):
		index_phrase=phrase[index]
		index_guest=guested_phrase[index]
		#
		if index_phrase in right_letters:
			new_guested.append(index_phrase)
			completed_chars+=1
		else:
			new_guested.append(index_guest)
		index+=1
	# print(new_guested)
	# print(completed_chars)
	guested_phrase=new_guested
	return 0

def print_monster()->None:
	for i in range(chars_by_errors*errors):
		if i>=len(monster):
			return
		print(monster[i],end='')
	print()
def display_situation()->None:
	print("This characters doesn't is in the phrase: ",end='')
	for i in no_chars:
		print(i,end=',')
	print()
	#
	for i in guested_phrase:
		print(i,end='')
	print()
###
def init_game_hangman(chance:int)->None:
	global phrase
	global cmd_hangman
	global guested_phrase
	global no_chars
	global completed_chars

	global chances
	global errors

	global monster
	global chars_by_errors

	cmd_hangman=["g"]
	no_chars=[]

	chances=chance
	errors=0

	monster="\\\\  //\n######\n#*#*##\n # #  "
	chars_by_errors=int(len(monster)/chances)
	completed_chars=0
	# print(monster)
	#
	file_temp=get_file()
	phrase=get_random_phrase(file_temp).lower()
	# print(phrase)
	guested_phrase=["_" if phrase[i].isalpha() else phrase[i] for i in range(len(phrase))]
	# print(guested_phrase)
	for i in phrase:
		if not i.isalpha():
			completed_chars+=1

def move_game_hangman(command:str)->int:
	command=command.split()
	if not len(command) or not command[0] in cmd_hangman:
		print("Invalid command")
	elif command[0] == "g":
		guess_word_hangman(command[1].lower())
	#
	print_monster()
	#
	if errors>=chances:
		print("You lost the game! The phrase is:\n{}".format(phrase))
		return -1
	if completed_chars == len(phrase):
		print("You win!")
		return 1
	return 0

def finish_game_hangman()->None:
	global phrase
	global cmd_hangman
	global guested_phrase
	global no_chars
	global completed_chars

	global chances
	global errors

	global monster
	global chars_by_errors

	del phrase
	del cmd_hangman
	del guested_phrase
	del no_chars
	del completed_chars

	del chances
	del errors

	del monster
	del chars_by_errors
###
""" COMMANDS
g [letters]     -> guest the select letters in phrase
"""
if __name__=="__main__":
	while True:
		print("========")
		init_game_hangman(5)
		while True:
			print("\n")
			display_situation()
			inp=input('*: ')
			#
			out=move_game_hangman(inp)
			# print(errors)
			if out:
				break

		finish_game_hangman()
