import random
import time

wordlist = ["blizzard", "your mother", "euan has no friends", "microwave", "oxygen", "absolute baller"]



hangmanpics = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\ |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']



def maingame():
    global answerword, wordguessed, hiddenword, wordpicked
    hiddenword = []
    guessedletters = []
    answerword = []

    wordguessed = False
    wordpicked = random.choice(wordlist)
    guessedwrong = 0
    for i in wordpicked:
        character = wordpicked[wordpicked.index(i)]
        if character.isspace() == False:
            hiddenword.append("_")
        else:
            hiddenword.append(",")

    answerword = "".join(str(e) for e in hiddenword)

    while wordguessed == False:
        letterwrong = True
        lettercorrect = False
        print(hangmanpics[guessedwrong])
        print(answerword, str(guessedwrong), "letters wrong")
        pickletter = input("Pick a random letter")
        while letterwrong == True:
            if pickletter.isalpha() == False or len(pickletter) >= 2 or len(pickletter) <= 0:
                pickletter = input("Invalid input, try again: ")
                letterwrong = True
            elif pickletter in guessedletters:
                pickletter = input("That letter has already been guessed, try again: ")
                letterwrong = True
            else:
                letterwrong = False

        for x in range(len(wordpicked)):
            if pickletter.lower() in wordpicked[x]:
                hiddenword[x] = pickletter
                guessedletters.append(pickletter)
                lettercorrect = True
        if lettercorrect == False:
            guessedwrong += 1

        answerword = "".join(str(e) for e in hiddenword)
        checkword()
        if guessedwrong >= 6:
            wordguessed = True
    if guessedwrong < 6:
        print(hangmanpics[guessedwrong])
        print("Congratulations! The word was", wordpicked, "and you guessed it with only", guessedwrong, "letters incorrect")
    else:
        print(hangmanpics[guessedwrong])
        print("You got too many wrong letters. The word was", wordpicked + ", better luck next time!")


def checkword():
    global wordguessed
    wordguessed = False
    counter = 0
    for i in range(len(wordpicked)):
        if hiddenword[i].isalpha() == True:
            counter += 1
        elif hiddenword[i] == ",":
            counter += 1
        if counter >= len(answerword):
            wordguessed = True

maingame()
while True:
    play = input("Do you want to play again? (y/n)")
    if play.lower() == "y":
        maingame()
    else:
        break