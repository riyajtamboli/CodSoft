import random

while True:
    actions = ['Rock', 'Paper', 'Scissors']
    Computer = random.choice(actions)
    print("********************************************")
    print("Rock-Paper-Scissors Game")
    print("Your turn::")
    your = input()
    print("Computer turn::")
    print(Computer)
    if (your == Computer):
        print("Tie!!")
    elif (your == 'Rock' and Computer == 'Scissors'):
        print("You Win!!")
    elif (your == 'Scissors' and Computer == 'Rock'):
        print("You lose!!")
    elif (your == 'Scissors' and Computer == 'Paper'):
        print("You Win!!")
    elif (your == 'Paper' and Computer == 'Scissors'):
        print("You lose!!")
    elif (your == 'Paper' and Computer == 'Rock'):
        print("You Win!!")
    elif (your == 'Rock' and Computer == 'Paper'):
        print("You lose!!")
    else:
        print("Enter Valid Choice.")

    ch = input("Do you want to Continue?(y/n)")
    if (ch == 'n'):
        print("Exiting")
        break
    elif (ch == 'y'):
        continue
    elif (ch != 'y'):
        print("Invalid Choice")
        break