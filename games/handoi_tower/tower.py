def decompositor_bin(number:int)->"array":
	array_num=[]
	while number>0:
	 	array_num.append(number%2)
	 	number//=2
	#
	temp=[]
	for i in range(len(array_num)):
	 	if array_num[i]:
		  	temp.append(2**i)
	if not len(temp):
	 	temp.append(0)
	array_num=temp
	return array_num
def check_round(index_1:int,index_2:int,table_conf:"array",discs_conf:"array")->int:
	disc_move=decompositor_bin(table_conf[index_1])
	disc_move=disc_move[0]
	#
	last_disc=decompositor_bin(table_conf[index_2])
	last_disc=last_disc[0]
	#
	if last_disc < disc_move and last_disc:
	 	print("Invalid move")
	 	return 0

	table_conf[index_1]-=disc_move
	table_conf[index_2]+=disc_move
	return 1
def display_table(table_conf:"array",max_disc:int):
	table_formated=[decompositor_bin(i) for i in table_conf]
	for i in table_formated:
		i.reverse()
	# print(table_formated)
	#
	temp=[['|' for j in range(max_disc)] for i in range(len(table_formated))]

	for i in range(max_disc):
		for j in range(len(table_formated)):
			if i >= len(table_formated[j]):
				continue
			temp[j][i]=table_formated[j][i]
	for i in range(len(temp)):
		temp[i].append('-')
		temp[i].append(i)
		temp[i].reverse()
	# print(temp)
	#
	table_formated=temp
	for i in range(len(table_formated[0])):
		for j in range(len(table_formated)):
			print(table_formated[j][i],end=' ')
		print()

def main_hanoi(disc:int,places:int)->int:
	array_discs=[2**i for i in range(disc)]
	array_table=[0 for i in range(places)]
	win=0
	#
	temp=0
	for i in array_discs:
	 	array_table[0]+=i
	 	win+=i
	#
	# print(array_discs)
	# print(array_table)
	# print(decompositor_bin(array_table[0]))
	#
	print("M -> Move a disc in the indexX to indexY\nH -> Help")
	display_table(array_table,disc)
	steps=0
	while True:
		steps+=1
		# print(array_table)
		inp=input('* ').split()
		if inp[0] == 'M' and len(inp)>2:
		  	check_round(int(inp[1]),int(inp[2]),array_table,array_discs)
		else:
		  	print("Invalid command")
		#
		# print(array_table)
		display_table(array_table,disc)
		if array_table[-1]==win:
			print("Congratulaions!!! You finish in {} steps in total".format(steps))
			break
if __name__=="__main__":
	main_hanoi(3,3)
