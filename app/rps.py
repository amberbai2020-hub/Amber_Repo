#Needs to re-organize code because the repeat test runs through all the code on the left margin, restuling in assert getting stuck on user input code

#Organization Structure: Import -> Functions -> 

#1. Import at the top

import random
#For modules and third-party packages, you both have to import to use it, but third-party packages must first be installed via Pip

#2. Followed by any constants

VALID_OPTIONS = ["rock", "paper", "scissors"]
#Upper case indicate that this is a constant

#3. Functions or classes

#4. Main conditional

if __name__ == "__main__":

    #Special if-statement at the bottom of your code
    #Only run the code if we execute the code from the command line, but not when we import from this file
    #Bypass the issue about the import statement

    # ASK USER FOR AN INPUT (R/P/S)

    user_choice = input("Please choose one of 'rock', 'paper', or 'scissors': ")
    print("USER:", user_choice)

    # VALIDATIONS

    if user_choice not in VALID_OPTIONS:
        print("OOPS INVALID INPUT, PLEASE TRY AGAIN")
        # exit()
        quit()

    # GENERATE RANDOM COMPUTER CHOICE

    computer_choice = random.choice(VALID_OPTIONS)
    print("COMP:", computer_choice)

    # DETERMINE THE WINNER

    # quick alias to facilitate some copy and pasting
    # we will soon move this into a function anyway
    u = user_choice
    c = computer_choice

    if u == "rock" and c == "rock":
        print("TIE GAME")
    elif u == "rock" and c == "paper":
        print("COMPUTER WINS")
    elif u == "rock" and c == "scissors":
        print("USER WINS")
    elif u == "paper" and c == "rock":
        print("COMPUTER WINS") # OOPS
    elif u == "paper" and c == "paper":
        print("TIE GAME")
    elif u == "paper" and c == "scissors":
        print("USER WINS") # OOPS
    elif u == "scissors" and c == "rock":
        print("COMPUTER WINS")
    elif u == "scissors" and c == "paper":
        print("USER WINS")
    elif u == "scissors" and c == "scissors":
        print("TIE GAME")