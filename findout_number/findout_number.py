import random
import subprocess

def generate_number()->int:
    dirs_home=subprocess.run(["ls","-R","/home"], capture_output=True,text=True)
    dirs_home=dirs_home.stdout
    dirs_home=dirs_home.split()
    chose_dir=(dirs_home[int(random.random()*len(dirs_home))])
    # print(chose_dir)
    return len(chose_dir)

def main_findout_number():
	print("\n")
	while True:
		random_num=int(generate_number()*random.random()*400)
		list_numbers=[{0:0}] # number X distance
		steps=0
		while True:
			steps+=1
			inp=input("*: ")
			big_distance=list(list_numbers[0].values())[0]
			big_distance_num=list(list_numbers[0].keys())[0]
			if inp=="p":
				print(big_distance)
				continue
			elif not inp[0].isdigit():
				print("Invalid command")
				continue
			#
			inp_int=int(inp)
			distance=1-abs(inp_int-random_num)/random_num
			distance*=100
			#
			if big_distance > distance:
				print("{} is more distant that {}".format(inp_int,big_distance_num))
			elif big_distance < distance:
				print("{} is more close that {}".format(inp_int,big_distance_num))
			else:
				print("{} is in same distance that {}".format(inp_int,big_distance_num))
			#
			stop=0
			for i in list_numbers:
				if inp_int==list(i.keys())[0]:
					stop=1
					break
			if stop:
				continue
			list_numbers.append({inp_int:distance})
			temp=sorted(list_numbers,key=lambda c:list(c.values())[0])
			temp.reverse()
			list_numbers=temp
			#
			if distance == 100:
				print("Congratulation!\nYou win the game with {} steps".format(steps))
				break

if __name__=="__main__":
    main_findout_number()
