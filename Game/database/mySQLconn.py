def mySQLrcv():
    "This is for retrieving past game details from database"

#Import modules and create dictionary
    import mysql.connector
    conDict = {"host":"localhost","database":"math_game","user":"root","password":""}

#Setup connection with database and collecct all the data and display it
    try:
        db = mysql.connector.connect(**conDict)
        print("\nConnection Successfull!")
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM past_player_details")
            data = cursor.fetchall()
            print("----------------------------------------------------------------------------------")
            print(":    Name    :  Game Mode  : Correct Questions : Total Questions : Percentage(%) :")
            print("----------------------------------------------------------------------------------")      
            for item in data:
                print(":",item[0]," "*(9-len(item[0])),":",item[1]," "*(10-len(str(item[1]))),":",item[2]," "*(16-len(str(item[2]))),":",item[3]," "*(14-len(str(item[3]))),":",item[4]," "*(12-len(str(item[4]))),":")
            print("----------------------------------------------------------------------------------")
        except:
            print("\n--- Error occurs in retrieving data ---")
        db.close()
    except:
        print("\n Oops! Connection Fails ")
        print("---BACKED TO MAIN MENU---")


