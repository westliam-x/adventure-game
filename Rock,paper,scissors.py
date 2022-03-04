import random

user_wins=0
com_wins=0
draw=0
options=["rock", "paper", "scissors"]

while True:
    user_input= input("Type rock,paper,scissors or Q to quit game. ").lower()
    if user_input=='q':
        break

    if user_input not in options:
        print("Input a valid option")
        continue
    
    random_number = random.randint(0,2)
    
    # rock:0, paper:1, scissors=2

    computer_input=options[random_number]
    print("computer picked", computer_input+ ".")

    if user_input== "rock" and computer_input=="scissors":
        print("You won!")
        user_wins+=1
        
    
    elif user_input== "paper" and computer_input=="rock":
        print("You won!")
        user_wins+=1
        
    
    elif user_input== "scissors" and computer_input=="paper":
        print("You won!")
        user_wins+=1
    elif user_input==computer_input:
        print("It's a tie")
        draw+=1
    else:
        print("You lost!")
        com_wins+=1
print("You won",user_wins, "times.")
print("You drew", draw ,"times")
print("Computer won",com_wins, "times.") 
print("goodbye!")
    
