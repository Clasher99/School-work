import time
import datetime
from random import randrange
import sqlite3

database = {
    "Adrian": "123",
    "Rafal": "1234",
    "Patryk": "12345",
    "Harry": "uhhh",
    "Josh": "phft",
    "doormat": "power2266",
    "geo egg": "eee",
    "euan": "sussy"
}

playersList = ['player1', "player2"]


def gamerules():
    print("")
    play = input("Here are the rules of the dice game, press enter after each step to go to the next one.")
    play = input("First, two players log into the game using a username and password stored in a database.")
    play = input("Once logged in, 5 rounds of dice rolling begin")
    play = input(
        "After pressing enter, two dice are rolled for each player. You can also exit the game at this stage if you want to.")
    play = input(
        "The two dice are added up. If the sum is even, 10 points are added on, but if it's odd, 5 points are taken off")
    play = input("If both dice are the same, an extra dice is rolled and added to their score for the current round")
    play = input(
        "After 5 rounds, all the scores from previous rounds are added up, and the player with the highest points wins the game")
    play = input(
        "The score is then stored in a database, and you can access the top scores from the main menu this way.")
    play = input(
        "Press enter again to go back to the main menu")
    time.sleep(1.5)


def leaderboards():
    mydb = sqlite3.connect('User_Data.db')
    mycursor = mydb.cursor()
    leaderboardnumber = input("How many top scores would you like? (Max 20): ")
    while leaderboardnumber.isnumeric() == False:
        leaderboardnumber = input("Invalid number, try again: ")
    while int(leaderboardnumber) > 20:
        leaderboardnumber = input("Too high, try again: ")
    selectString = "SELECT name, points, date from Dice_Game ORDER BY points desc limit "
    mycursor.execute(selectString + leaderboardnumber)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
        time.sleep(0.5)


def playAgain():
    print("""
            1: Play again
            2: Play again with different players
            3: Leaderboards
            4: Exit Program
            """)

    playagain = input("Enter your choice [1-4]:")
    if playagain == "1":
        dicegame()
    elif playagain == "2":
        print("")
        time.sleep(2)
        login()
        dicegame()
    elif playagain == "3":
        leaderboards()
    elif playagain == "4":
        exit()
    else:
        print("Invalid input, try again: ")


def menu():
    loop = True
    while loop:
        print("""
            1: Play the Dice Game
            2: Leaderboards
            3: Read the game rules
            4: Exit Program
            """)
        choice = input("Enter your choice [1-3]:")
        if choice == "1":
            login()
            dicegame()
        elif choice == "2":
            print("")
            leaderboards()
        elif choice == "3":
            gamerules()
        elif choice == "4":
            loop = False
        else:
            print("Wrong option, try again")


def login():
    for x in playersList:
        username = input("Player " + str(playersList.index(x) + 1) + " Enter Name: ")
        counter = 0
        while username not in database and counter < 4:
            username = input("Wrong username, try again: ")
            counter += 1
            if counter == 4:
                print("Too many wrong attempts. Goodbye.")
                exit()
        password = input("Player " + str(playersList.index(x) + 1) + " Enter Password: ")
        counter = 0
        while password != database[username] and counter < 4:
            password = input("Incorrect password, try again: ")
            counter += 1
            if counter == 4:
                print("Too many wrong attempts. Goodbye.")
                time.sleep(1.5)
                exit()
        print("Hello " + username)
        playersList[playersList.index(x)] = username


def dicegame():
    global sumScore, z
    player1dice = [0, 0]
    player2dice = [0, 0]
    playersDices = [player1dice, player2dice]
    player1Score = 0
    player2Score = 0
    playertotal1 = 0
    playertotal2 = 0
    player1final = 0
    player2final = 0
    playersScores = [player1Score, player2Score]
    playerTotals = [playertotal1, playertotal2]
    playerFinalScores = [player1final, player2final]
    time.sleep(1)
    for i in range(5):
        print("")
        print("Round " + str(i + 1))
        time.sleep(1.5)
        print("")
        for y in range(len(playersList)):
            play = input(playersList[y] + ", press enter to roll the dice, or press 1 to go back to main menu ")
            if play == "1":
                playAgain()
            print("")
            print("Rolling...")
            time.sleep(3)
            sumScore = 0
            print("")
            for z in range(len(playersDices[y])):
                player = randrange(1, 6)
                playersDices[y][z] = player
                sumScore += player
            print(playersList[y], "rolled", str(playersDices[y][0]), "and",
                  str(playersDices[y][1]), "and got a total of", str(
                    sumScore), "points")
            if sumScore % 2 == 0:
                sumScore += 10
                time.sleep(3)
                print(playersList[y] + "'s roll was even, so their score goes up to", sumScore, "points")
            else:
                sumScore -= 5
                if sumScore <= 0:
                    sumScore = 0
                time.sleep(3)
                print(playersList[y] + "'s roll was odd, so their score goes down to", sumScore, "points")

            playersScores[y] = sumScore
            playerTotals[y] += sumScore

            time.sleep(3)
            if playersDices[y][0] == playersDices[y][1]:
                print("")
                time.sleep(2)
                a = randrange(1, 6)
                playersScores[y] += a
                playerTotals[y] += a
                play = input(playersList[y] + ", you rolled a double so press enter to roll an extra dice")
                print("")
                print("Rolling...")
                print("")
                time.sleep(1.5)
                print(str(playersList[y]) + " rolled an extra " + str(
                    a) + ", bringing their score to " + str(playersScores[y]))
                time.sleep(2)
            print("")

    print("")
    print("The dice game has ended! Here are the results:")
    time.sleep(1.5)

    winplayer = ""
    winscore = 0
    for x2 in range(len(playersList)):
        print(str(playersList[x2]) + " got " + str(playerTotals[x2]) + " points")
        time.sleep(2)
        if playerTotals[x2] == 69:
            print("Nice")
    if playerTotals[0] > playerTotals[1]:
        print(playersList[0] + " wins by " + str((playerTotals[0] - playerTotals[1])) + " points")
        winplayer = playersList[0]
        winscore = playerTotals[0]
    elif playerTotals[1] > playerTotals[0]:
        print(playersList[1] + " wins by " + str((playerTotals[1] - playerTotals[0])) + " points")
        winplayer = playersList[1]
        winscore = playerTotals[1]
    time.sleep(5)

    if playerTotals[0] == playerTotals[1]:
        time.sleep(2)
        print("")
        print("Both players got the same score so they both roll an extra dice to decide the winner")
        time.sleep(2)
        endgame = False
        while endgame == False:
            for x4 in range(2):
                finaldice = randrange(1, 6)
                playerFinalScores[x4] = finaldice
                print("")
                play = input(playersList[x4] + ", press enter to roll your final dice")
                time.sleep(2)
            if playerFinalScores[0] > playerFinalScores[1]:
                endgame = True
                print(playersList[0] + " got " + str(playerFinalScores[0]) + " and " + playersList[1] + " got " + str(
                    playerFinalScores[1]) + " so " + playersList[0] + " wins! ")
                winplayer = playersList[0]
                winscore = playerTotals[0]
                time.sleep(3)
                break
            elif playerFinalScores[1] > playerFinalScores[0]:
                endgame = True
                print(playersList[0] + " got " + str(playerFinalScores[0]) + " and " + playersList[1] + " got " + str(
                    playerFinalScores[1]) + " so " + playersList[1] + " wins! ")
                winplayer = playersList[1]
                winscore = playerTotals[1]
                time.sleep(3)
                break
            else:
                print("Both players got", str(playerFinalScores[0]) + ", so they roll again.")
                time.sleep(3)

    now = datetime.datetime.now()
    dt_string = now.strftime("%H:%M on %d/%m/%Y")

    insertVariableIntoTable(winplayer, winscore, dt_string)
    playAgain()


def createDatabaseRunOnce():
    try:
        sqliteConnection = sqlite3.connect('User_Data.db')
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS Dice_Game (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    points INTEGER NOT NULL,
                                    date datetime);'''
        cursor = sqliteConnection.cursor()
        cursor.execute(sqlite_create_table_query)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)


createDatabaseRunOnce()


def insertVariableIntoTable(name, points, date):
    try:
        sqliteConnection = sqlite3.connect('User_Data.db')
        cursor = sqliteConnection.cursor()
        sqlite_insert_with_param = """INSERT INTO Dice_Game
                          (name, points, date)
                          VALUES (?, ?, ?);"""
        data_tuple = (name, points, date)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)


menu()
