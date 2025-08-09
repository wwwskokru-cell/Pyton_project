
import random

stone = "stone"
scissors = "scissors"
paper = "paper"
my_list = [stone, scissors, paper]
choice_me = random.choice(my_list)
win = "YOU WIN"
loss = "You've lost! try again"
choice = input(" Election of the stone, scissors, paper: ")
if choice in my_list:
    if choice_me == choice:
        print ("draw")
    elif choice_me == my_list[0] and choice == "paper":
        print (win)
    elif choice_me == my_list[0] and choice == "scissors":
        print (loss)
    elif choice_me == my_list[1] and choice == "paper":
        print (loss)
    elif choice_me == my_list[1] and choice == "stone":
        print (win)  
    elif choice_me == my_list[2] and choice == "stone":
        print (loss)
    elif choice_me == my_list[2] and choice == "scissors":
        print (win)     
else:
    print("error")