import random

user_wins = 0
computer_wins = 0
Draws = 0

Options = ["rock","paper","scissors"]

while True:
    user_input = input("Type Rock\Paper\Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in Options:
        continue

    random_number = random.randint(0,2)
    #Rock:0 #Paper:1 #Scissors:2
    computer_pick = Options[random_number]
    print("Computer picked ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You Win!")
        user_wins +=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Wins!")
        user_wins +=1

    elif user_input == "rock" and computer_pick == "rock":
        print("Draw!")
        Draws += 1

    elif user_input == "paper" and computer_pick == "paper":
        print("Draw!")
        Draws +=1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Draw!")
        Draws +=1    
    
    else:
        print("You Lost!")
        computer_wins +=1

print("You won", user_wins,"times")
print("The Computer Won",computer_wins,"times")
print("Draws",Draws,"times")
print("Good Bye!")               

