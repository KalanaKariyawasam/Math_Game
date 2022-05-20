#Game menu

#Import modules
import sys
import QuickGame.QuickGame
import CustomGame.CustEasy
import CustomGame.CustMedium
import CustomGame.CustHard
import CustomGame.CustDiff
import database.mySQLconn
import database.mySQLdlt

#Creating Main Menu
print("\n***WELCOME TO THE MATH GAME***")
while True:
    print("\n-----MAIN MENU-----\n")
    print("a) Quick Game")
    print("b) Custom Game")
    print("c) Past Game Details")
    print("d) Delete Past Game Details")
    print("e) Exit\n")
#Get user inputs
    option1 = input("Enter your option : ")

    if(option1 == "a"):
        QuickGame.QuickGame.QGame()
    elif(option1 == "b"):
        #Creating Custom Menu
        while True:
            print("\n-----CUSTOM MENU-----\n")
            print("a) Easy")
            print("b) Medium")
            print("c) Hard")
            print("d) Difficult")
            print("e) Exit\n")
            #Get user inputs
            option2 = input("Enter your dificulty level or exit : ")

            if(option2 == "a"):
                CustomGame.CustEasy.easy()
            elif(option2 == "b"):
                CustomGame.CustMedium.medium()
            elif(option2 == "c"):
                CustomGame.CustHard.hard()
            elif(option2 == "d"):
                CustomGame.CustDiff.difficult()
            elif(option2 == "e"):
                break
            else:
                print("\nInvalid Option! ---BACKED TO CUSTOM MENU---")
                
        print("\n-----BACK TO MAIN MENU-----")

    elif(option1 == "c"):
        database.mySQLconn.mySQLrcv()
    elif(option1 == "d"):
        database.mySQLdlt.mySQLdlt()
    elif(option1 == "e"):
        print("\n---END OF THE GAME---")
        break
    else:
        print("\nInvalid Option! ---BACKED TO MAIN MENU---")
