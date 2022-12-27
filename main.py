import random

#UI
print("**** WELCOME TO HANGMAN ****")
print(
    "You have 6 tries to guess the word. The theme is animals! Please type your guesses using capital letters"
)

#Variables
wordBank = ("PYTHON", "FISH", "DOLPHIN", "GORILLA", "GIRAFFE")
word = random.choice(wordBank)
wordArr = list(word)
space = "_"
wordLen = len(word)
boardArr = list(space * wordLen)
tries = 6
guessedLetters = list()

#Print Hangman Board
def printBoard(L):
  for i in range(6, -1, -1):
      for j in range(7):
          print(L[j][i], end="")
      print(" ")

#Setup the Hangman Board
def hangmanBoardSetup():
  a = 0
  b = 0
  L = []
  for x in range(7):
    L.append([])
    for y in range(7):
      L[x].append(" ")
  
  for i in range(7):
    L[a][b] = "|"
    L[3][5] = "|"
    b += 1
  
  for i in range(7):
    L[a][0] = "-"
    L[a][6] = "-"
    a += 1
    
  if tries == 5:
    L[3][4] = "O"
  elif tries == 4:
    L[3][4] = "O"
    L[3][3] = "|"
  elif tries == 3:
    L[3][4] = "O"
    L[3][3] = "|"
    L[2][3] = "/"
  elif tries == 2:
    L[3][4] = "O"
    L[3][3] = "|"
    L[2][3] = "/"
    L[4][3] = "\\"
  elif tries == 1:
    L[3][4] = "O"
    L[3][3] = "|"
    L[2][3] = "/"
    L[4][3] = "\\"
    L[2][2] = "/"
  elif tries == 0:
    L[3][4] = "O"
    L[3][3] = "|"
    L[2][3] = "/"
    L[4][3] = "\\"
    L[2][2] = "/"
    L[4][2] = "\\"
  printBoard(L)

#Game
def gameSequence():
    print("\n")
    print(*boardArr, sep=" ")
    print("\n")
    print("1. Guess a letter")
    print("2. Solve the word")
    option = int(input("Option: "))

    if option == 1:
        guess = input("\nPlease enter your guess: ")
        while guess.isalpha() == False:
          print("Sorry that was an invalid input! Please try again!")
          guess = input("\nPlease enter your guess: ")
        while len(guess) > 1:
          print("Sorry, you can only guess one letter! Please try again!")
          guess = input("\nPlease enter your guess: ")
    elif option == 2:
        solve = input("\nSolve the word: ")
        if solve == word:
            print("CONGRATULATIONS YOU HAVE WON THE GAME!!!")
            exit()

    if guess in wordArr:
        for i in range(len(wordArr)):
            if wordArr[i] == guess:
                boardArr[i] = guess
        hangmanBoardSetup()
        gameSequence()
    elif guess not in wordArr:
        print("Sorry, that letter is not in the word.")
        global tries
        tries = tries - 1
        hangmanBoardSetup()
        print("Number of tries left: " + str(tries))
        guessedLetters.append(guess)
        print("Guessed Letters: " + str(guessedLetters))
        gameSequence()
    if tries == 0:
        print("YOU HAVE LOST THE GAME")
        exit()
gameSequence()
