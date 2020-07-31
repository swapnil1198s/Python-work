##name: Swapnil Srivastava
##hangman.py
##
##problem: This program takes the input string from
##            the user and checks if the letter entered matches
##            a randomly chosen word. Then it continues to play hangman
##
##Certificate of Authenticity:
##    I certify that this is entirely my own work.

#import graphics for the graphical interface
##import random and math from their libraries
import random
import graphics

from graphics import *

import math

##function to read the wordfile
def readFile():
    infile = open("wordlist.txt", "r")
    wordList = []
    for line in infile:
        string = line.split()
        wordList += string
##return the wordfile content as a list 
    return wordList

##function to choole a random line a.k.a random word
def randomLine(wordList):
    num = random.randint(0, len(wordList)-1)
    randomWord = wordList[num]
##return a random word from the list
    return randomWord

##function to check if the entered letter is correct
def guessedWord(word, guess, blanks):
    count = 0
    blanks = blanks.split()
##loop through the entire word to check if any letter matches
    for i in range(len(word)):
       item = word[i]
       blankitem = blanks[i]
       if blankitem != guess and item == guess:
           blanks.pop(i)
           blanks.insert(i, guess)
##return the blanks with the letter if it is correct
    return " ".join(blanks)

##function to determine if the game has been won
def win(checkguess, word):
##check if the letters guessed spell out the word
    checkguess = checkguess.replace(" ", "")
##return true if the game has been won or return false
    if str(checkguess) == str(word):
        return True
    else:
        return False

##function to play the game    
def playgame():
##draw the graphics window
    winWidth = 600
    winHeight = 400
    window = GraphWin("Hangman", winWidth, winHeight)
##make the body parts for the hangman
    head = Circle(Point(winWidth - 30, winHeight-350), 20)
    body = Line(Point(winWidth - 30, winHeight-350),
                Point(winWidth - 30, winHeight-250))
    leg =  Line(Point(winWidth - 30, winHeight-250),
                Point(winWidth - 50, winHeight-200))
    rleg =  Line(Point(winWidth - 30, winHeight-250),
                 Point(winWidth - 10, winHeight-200))
    hand = Line(Point(winWidth - 30, winHeight-300),
                Point(winWidth - 10, winHeight-250))
    lhand = Line(Point(winWidth - 30, winHeight-300),
                 Point(winWidth - 50, winHeight-250))
    rope = Line(Point(winWidth - 30, winHeight-370),
                Point(winWidth - 30, 0))
    
##text instructions for the game
    instructions = Text(Point(winWidth/2, winHeight - 30),
                        "Lets play hangman!")
    instructions.draw(window)
##text for after the game is finished
    yes = Rectangle(Point(winWidth/2 - 100, winHeight-150),
                    Point(winWidth/2 - 150, winHeight-120))
    yesQ = yes.getCenter()
##assign where the blanks for the word will be on the graphics window
    blankWord = Text(Point(winWidth/2+45, winHeight-350), 30)
    Text(Point(winWidth/2 - 160, winHeight-350),
                        "Word: ").draw(window)
##assign where the textbox for entering the letter will be
    Text(Point(winWidth/2 - 160, winHeight-250),
                        "Guess Word: ").draw(window)
    guess = Entry(Point(winWidth/2+45, winHeight-250), 30)
    guess.setText("")
    guess.draw(window)
##make the list of words
    wordList = readFile()
##choose a random word from list
    word = randomLine(wordList)
##display blanks for the chosen words
    blanks = str("_ ")*len(word)
    guess.setText("")
##check if the guessed letter is correct
    checkguess = guessedWord(word, guess, blanks)
##check if the word has been guessed
    checkCorrection = win(checkguess, word)
    count = 0
    blankWord.setText(blanks)
    blankWord.draw(window)
##assign string to be used later
    playAgain = "If yes, click button. If not, click anywhere to close."
##loop to give player 7 guesses
    while checkCorrection!=True and count<11:
##        input letter by the user
        guess1 = str(guess.getText())
##        check if guess is correct
        checkguess = guessedWord(word, guess1, checkguess)
        blankWord.setText(checkguess)
##        loop to reduce count 
        for i in range(len(word)):
            item = word[i]
            blankitem = blanks[i]
            if blankitem != guess1 and item == guess1:
                count = count-1
##        statements to draw the hangman parts based on count
        if (7-(math.fabs(count))) == 6:
            rope.draw(window)
        elif (7-(math.fabs(count))) == 5:
            head.draw(window)
            head.setFill("red")
        elif (7-(math.fabs(count))) == 4:
            body.draw(window)
        elif (7-(math.fabs(count))) == 3:
            lhand.draw(window)
        elif (7-(math.fabs(count))) == 2:
            hand.draw(window)
        elif (7-(math.fabs(count))) == 1:
            leg.draw(window)
        checkCorrection = win(checkguess, word)
##        check if the game has been won
        if checkCorrection == True:
            instructions.setText("Game has been won! Click to close")
            
        else:
##            print tries left
            tries = ("Tries left: " + str(int(7-(math.fabs(count))))
                     + "; Click to continue")
            instructions.setText(tries)
            window.getMouse()
        count += 1
##         check if the game has been lost
        if count==7:
            instructions.setText("You lost! Click to close")
            rleg.draw(window)

    yes.draw(window)
##    ask if the player wants to play again
    Text(Point(winWidth/2 - 60, winHeight-200),
                "Do you want to play again?").draw(window)
    
    Text(Point(winWidth/2 - 60, winHeight-180),
                playAgain).draw(window)
    chooseYes = Text(yesQ, "Yes")
    chooseYes.draw(window)
    again = window.getMouse()
##    determine if the area of click is within the button 
    x = again.getX()
    y = again.getY()
    sqx = (x - 175)**2
    sqy = (y - 265)**2
##if the click was in the button then close the current window
##    and play game again
    if math.sqrt(sqx + sqy) < 100:
        window.close()
        playgame()
##    if the click was outside the button then close window
    else:
        window.close()

playgame()
##def main():
##    wordList = readFile()
##    word = randomLine(wordList)
##    print(word)
##    return word

    

