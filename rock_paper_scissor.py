import random

while True:
    possible_outcome=("Rock","Paper","Scissor")
    computer_action=random.choice(possible_outcome)
    user_action=input("Enter a choice (Rock,Paper,Scissor): ")
    print(f"\n You choose {user_action} & computer choose {computer_action}.\n")

    if computer_action==user_action:
        print(f"Both player selected {user_action}.Its a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissor":
            print("Rock smashes Scissor.\n You Win!")
        else:
            print("Paper covers Rock! \n You Loose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock.\n You Win!")
        else:
            print("Scissor cuts Papaer! \n You Loose.")
    elif user_action == "Scissor":
        if computer_action == "Paper":
            print("Scissor cuts Papers! \n You Win. ")
        else:
            print("Rock smashes Scissor! \n You Loose. ")

    play_again=input("Play Again? (y/n): ")
    if play_again.lower() != "y":
        break


