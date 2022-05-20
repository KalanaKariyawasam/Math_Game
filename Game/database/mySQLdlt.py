def mySQLdlt():
    "This is for delete past game details from the database"

#Import modules and create dictionary
    import mysql.connector
    conDict = {"host":"localhost","user":"root","password":"","database":"math_game"}

#Setup connection with database and delete all the data
    try:
        db = mysql.connector.connect(**conDict)
        print("Connection Successful")
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM past_player_details")
            db.commit()
            print(cursor.rowcount, "Record(s) deleted!")
        except:
            print("Error ocuurs in deleting data")
        db.close()
    except:
        print("\n Oops! Connection Fails ")
        print("---BACKED TO MAIN MENU---")

