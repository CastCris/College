def check_score(answer_user_list, answer_list):
    score = 0
    for i in range(len(answer_list)):
        if answer_user_list[i] == answer_list[i]:
            score += 1
    return score

def get_valid_answer(question_text):
    while True:
        answer = input(question_text).lower()
        if answer in ["a", "b", "c", "d", "e"]:
            return answer
        else:
            print("Please enter a valid option: a, b, c, d, or e.")

answer_list = ["d", "c", "a", "e", "e", "b", "b", "d", "c"]


print("Welcome to the interactive quiz!\nYou'll answer a bunch of questions and at the end you'll receive your score based on your corrected answers.")

i = "y"
while i == "y":
    answer_user_list = []

    questions = [
        "\n1. What's the largest animal species currently alive?\na) African elephant\nb) Colossal squid\nc) Great white shark\nd) Blue whale\ne) Sperm whale\n\nAnswer: ",
        "\n2. What animal must sleep standing up?\na) Kangoroo\nb) Elephant\n c)Horse\nd) Frog\n e) Monkey: ",
        "\n3. What's the capital of Australia?\na) Canberra\nb) Melbourne\nc) Sydney\nd) Brisbane\ne) Perth\n\nAnswer: ",
        "\n4. Who wrotes the play Romeo and Julieta?\na) Edgar Allan Poe\nb) Jane Austen\nc) Charles Dickens\nd) Leo Tolstoy\ne) William Shakespeare\n\nAnswer: ",
        "\n5. What does HTTP stand in a website adress?\na) Hyper Text Transmission Protocol\nb) Hyper Tool Transfer Protocol\nc) Hyperlink and Text Transfer Protocol\nd) Hyper Terminal Transfer Protocol\ne) Hyper Text Transfer Protocol\n\nAnswer: ",
        "\n6. What does HTTPS add to HTTP?\na) Faster loading\nb) Encryption using SSL/TLS\nc) Compatibility with firewalls\nd) Data compression\ne) Mobile optimization\n\nAnswer: ",
        "\n7. What's the primary goal of a DDoS attack?\na) Encrypt data for ransom\nb) Overload a system to disrupt service availability\nc) Gain unauthorized acess to user accounts\nd) Redirect traffic to malicious websites\ne) Intercept private messages\n\nAnswer: ",
        "\n8. How does the cluster size affect disk performance?\na) Larger clusters cause slow read/write speeds\nb) Smaller clusters always improve speed by storing more files per cluster\nc) Smaller clusters cause more fragmentation and slow down the disk\nd) Larger clusters improve speed by reducing the number of clusters to manage\ne) Cluster size has no effect on disk speed\n\nAnswer: ",
        "\n9. What's the main cause of wasted disk space in relation to cluster size?\na) Files being compressed incorrectly\nb) Files too large to fit into a single cluster\nc) Files smaller than the cluster size occuping a full cluster\nd) Overlapping files in the file system\ne) Defragmentation process\n\nAnswer: "
    ]

    for q in questions:
        answer_user_list.append(get_valid_answer(q))

    answer_list_dic = []
    answer_user_list_dic = []
    for i in range(len(answer_list)):
        answer_list_dic.append({f"{i + 1}.": answer_list[i]})
        answer_user_list_dic.append({f"{i + 1}.": answer_user_list[i]})

    print("\nYour answers:\n", answer_user_list_dic)

    score = check_score(answer_user_list, answer_list)
    print(f"\n=============\nScore: {score} /", len(questions), "\n=============\n")

    i = input("\nPress (y) to play again\nPress (a) to view the answer list\nPress any key to exit\n").lower()

    if i == "a":
        print("\nCorrect answers:\n", answer_list_dic)
        i = input("\nPress (y) to play again\nPress any key to exit\n").lower()
