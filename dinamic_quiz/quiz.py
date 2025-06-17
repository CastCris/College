print("Welcome to the interative quiz!\nYou'll answer a bunch of questions and at the end you'll receive your score based on your corrected answers.\n")

def check_score(answer_user, answer):
    if (answer_user == answer):
        return 1
    return 0

i = "y"
while (i == "y"):
    score = 0

    answer_user = input("1. What's the biggest animal?\na) bear\nb) snake\nc) bird\nd) shark\ne) frog\nAnswer: ");answer_user = answer_user.lower()
    score += check_score(answer_user, "d")








    print(f"Score: {score}")
    i = input("Do you wanna to play again?\nPress (y) to play again\nPress any key to exit\n");i = i.lower()