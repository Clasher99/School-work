import time

row1 = ["1", "2", "3"]
row2 = ["4", "5", "6"]
row3 = ["7", "8", "9"]

symbols = ["X", "O"]
winsymbol = [""]
gamefinished = False


def printgrid():
    print("  ", row1[0], "  ", row1[1], "  ", row1[2])
    print("  ", row2[0], "  ", row2[1], "  ", row2[2])
    print("  ", row3[0], "  ", row3[1], "  ", row3[2])


def checkgrid():
    global winsymbol
    global gamefinished
    for x in symbols:
        current = symbols[symbols.index(x)]
        if current == row1[0] == row1[1] == row1[2]:
            gamefinished = True
            winsymbol = current
        elif current == row2[0] == row2[1] == row2[2]:
            gamefinished = True
            winsymbol = current
        elif current == row3[0] == row3[1] == row3[2]:
            gamefinished = True
            winsymbol = current
        elif current == row1[0] == row2[0] == row3[0]:
            gamefinished = True
            winsymbol = current
        elif current == row1[1] == row2[1] == row3[1]:
            gamefinished = True
            winsymbol = current
        elif current == row1[2] == row2[2] == row3[2]:
            gamefinished = True
            winsymbol = current
        elif current == row1[0] == row2[1] == row3[2]:
            gamefinished = True
            winsymbol = current
        elif current == row1[2] == row2[1] == row3[0]:
            gamefinished = True
            winsymbol = current


def maingame():
    resetgrid()
    global currentplay
    counter = 0
    while not gamefinished:
        if counter % 2 == 0:
            currentplay = "X"
        else:
            currentplay = "O"
        printgrid()
        global play
        play = input("Player with symbol " + str(currentplay) + ", pick a number on the grid:")
        while play.isnumeric() == False or int(play) > 9 or int(play) < 0 or len(play) > 2:
            play = input("Invalid input, try again")
        counter += 1
        changegrid()
        checkgrid()

        if counter == 9:
            break

    if winsymbol == "X":
        printgrid()
        time.sleep(2)
        print("Player with symbol X wins")
    elif winsymbol == "O":
        printgrid()
        time.sleep(2)
        print("Player with symbol O wins")
    else:
        printgrid()
        time.sleep(2)
        print("No one wins")


def changegrid():
    global invalidmove, play
    invalidmove = True
    while invalidmove:
        for i in row1:
            if play == (row1[row1.index(i)]):
                row1[row1.index(i)] = currentplay
                invalidmove = False
        for i in row2:
            if play == (row2[row2.index(i)]):
                row2[row2.index(i)] = currentplay
                invalidmove = False
        for i in row3:
            if play == (row3[row3.index(i)]):
                row3[row3.index(i)] = currentplay
                invalidmove = False
        if invalidmove == True:
            play = input("That space is already taken, try again: ")

def resetgrid():
    global gamefinished
    row1[0] = "1"
    row1[1] = "2"
    row1[2] = "3"
    row2[0] = "4"
    row2[1] = "5"
    row2[2] = "6"
    row3[0] = "7"
    row3[1] = "8"
    row3[2] = "9"

    gamefinished = False


def menu():
    loop = True
    while loop == True:
        playgame = input("Would you like to play noughts and crosses (1) or exit (2)?")
        if playgame == "1":
            time.sleep(1)
            maingame()
        elif playgame == "2":
            exit()
        else:
            print("Invalid input, try again")

print("")
menu()
