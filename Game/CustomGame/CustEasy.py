def easy():
    "This is for Easy Game Mode"

    #Import modules and create variables
    import random
    import mysql.connector
    global tot
    name = ""
    mode = "Easy"
    question = ""
    playerdetails = []
    num1 = 0
    num2 = 0
    count = 1
    tot = 0
    qnum = 0
    precentage = 0
    
#Get user inputs
    name = input("Enter your name : ")
    qnum = input("How many questions you need? : ")
    print("\n")

#Process
    while(count<=int(qnum)):
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
        question = input("Q"+str(count)+": "+str(num1)+" + "+str(num2)+" = ")

        if(int(question) == (num1+num2)):
            playerdetails.append(("Q"+str(count)+": "+str(num1)+" + "+str(num2)+" = "+str(question)+" (Correct Answer "+str(num1+num2)+")"+" Correct"))
            tot += 1
            count += 1

        else:
            playerdetails.append(("Q"+str(count)+": "+str(num1)+" + "+str(num2)+" = "+str(question)+" (Correct Answer "+str(num1+num2)+")"+" Incorrect"))
            count += 1       
#Output
    print("\nYour name is",name)
    print("You played the game with",mode,"Mode")
    print("You answered",qnum,"questions\n")

    for item in playerdetails:
            print(item)
    print("\nCorrect Answers : ",tot)
    precentage = (int(tot)/int(qnum))*100
    print("Your results percentage is",precentage,"%")

#Insert Values to the databse
    conDict = {"host":"localhost","user":"root","password":"","database":"math_game"}
    
    try:
        db = mysql.connector.connect(**conDict)
        print("Connection Successful")
        cursor = db.cursor()
        try:
            mySQLtxt = "INSERT INTO past_player_details (name,gamemode,correctquestions,totalquestions,precentage) VALUES (%s,%s,%s,%s,%s)"
            myValues = (name,mode,tot,qnum,precentage)
            cursor.execute(mySQLtxt,myValues)
            db.commit()
            print(cursor.rowcount, "Record added to Database")
        except:
            print("Error ocuurs in inserting data")
        db.close()
    except:
        print("Connection Fails")
    

