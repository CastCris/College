import random
import subprocess

def generate_number()->int:
    dirs_home=subprocess.run(["ls","-R","/home"], capture_output=True,text=True)
    dirs_home=dirs_home.stdout
    dirs_home=dirs_home.split()
    chose_dir=(dirs_home[int(random.random()*len(dirs_home))])
    # print(chose_dir)
    return len(chose_dir)
def view_list(list_numbers:"list",*args):
    amount_items=0
    if len(args):
        amount_items=args[0]
    else:
        amount_items=len(list_numbers)
    #
    if amount_items>len(list_numbers):
        amount_items=len(list_numbers)
    #
    sorted_list=sorted(list_numbers,key=lambda c:list(c.values())[0])
    sorted_list.reverse()
    print("number \t distance")
    for i in range(amount_items):
        print("{} \t {:.10f}".format(list(sorted_list[i].keys())[0],list(sorted_list[i].values())[0]))


print("Hello!\nWelcome to findout number game!\nIn this game, your aim is discover the number by of information given by an entried number. Each number inputed, is print a float value. This means how much longer the entered number is of the random number in porcentage.\nThe distance is calculate through the operation: abs(inputed_number-random_number)/random_number")
print("\n\n")
commands="H-> display this menu\nv [amount_items]-> view the list of biggest porcentage\n"
print(commands)
while True:
    random_num=int(generate_number()*(random.random()*400))
    # print(random_num)
    list_biggest=[]
    try:
        while True:
            inp=input("* ").split()
            if not len(inp):
                continue
            if inp[0] == "v" and len(inp)>1:
                view_list(list_biggest,int(inp[1]))
                continue
            elif inp[0]=="v" and len(inp)<2:
                view_list(list_biggest)
                continue
            elif not inp[0][0].isdigit:
                print("Invalid command")
                continue
            #
            inp_int=int(inp[0])
            distance=1-abs(random_num-inp_int)/random_num
            distance*=100

            list_biggest.append({inp_int:distance})
            print(distance)
            if distance==100:
                print("Congratulation!!!\nYou win after {} try".format(len(list_biggest)))
                break
    except KeyboardInterrupt:
        break
