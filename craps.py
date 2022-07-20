import random

def roll_the_dice():
    "use random to add 2 random dice values for the game"
    return (random.randint(1,6) + random.randint(1,6))

def craps():
    "initializes the number to the number generated in the function roll_the_dice()"
    number = roll_the_dice()
    print("player rolled: ", number)
    if(number == 7 or number == 11):
        print("you win!")
    elif (number == 2 or number == 3 or number == 12):
        print("you lose.")
    else:
        points = number
        print("Point to hit is: ", points)
        newnumber = 0
        while (newnumber != points and newnumber != 7):
            newnumber = roll_the_dice()
            print("you rolled: ", newnumber)
            if (newnumber == points):
                print("you win!")
            elif (newnumber == 7):
                print("you lose")
            else:
                print("roll again")
craps()