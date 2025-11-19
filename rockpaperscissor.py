import random
def getuserchoice():
    userchoice = input("Enter your choice rock/paper/scissors.").lower()
    while userchoice not in["rock","paper","scissors"]:
        userchoice = input("Enter your choice rock/paper/scissors.").lower()

    return userchoice

def getcomputerchoice():
    return random.choice(["rock","paper","scissors"])

def playgame():
    print("Welcome to rock paper scissors...")
    userchoice = getuserchoice()
    computerchoice = getcomputerchoice()
    print("You chose",userchoice)
    print("Computer chose",computerchoice)
    result = determinewinner(userchoice, computerchoice)
    print (result)


        return ("It's a tie!")

    elif (userchoice == "rock" and computerchoice == "scissors") or (userchoice == "paper" and computerchoice == "rock") or (userchoice == "scissors" and computerchoice == "paper"):
        return "you win"
    else:
        return "computer wins"
    
playgame()