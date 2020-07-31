##name: Swapnil Srivastava
##vigenere.py
##
##problem: This program takes the input string from
##            the user and outputs a encoded message
##
##Certificate of Authenticity:
##    I certify that this is entirely my own work.

#import graphics for the graphical interface
import graphics

from graphics import *

#method to encode the given string using a keyword
def code(message, keyword):

#split the string into different words
    message = message.split(" ")
#join the words without spaces
    message = "".join(message)
#convert the string to upper case
    message = message.upper()
#get lengths of string and keyword for the loop
    length = len(message)
    keylength = len(keyword)
#define the variable for encrypted message
    string = ""
    x = 0

    keyword = keyword.upper()

#loop to get the encrypted message
    for ch in message:
        num = (((ord(ch) + (ord(keyword[x%keylength])))-ord("A")
                - 13)%26) + ord("A")
        x +=1
        
        string += str(chr(num))
#return the encrypted message
    return string
    

def main():

#create a graphics window
    winWidth = 600
    winHeight = 400
    win = GraphWin("Vigenere", winWidth, winHeight)
#instructions on when to click
    instructions = Text(Point(winWidth/2, winHeight - 30),
                        "Click to encrypt message")
    instructions.draw(win)
#textfields and lables for string and keyword
    message = Entry(Point(winWidth/2+45, winHeight-350), 30)
    message.setText("")
    message.draw(win)
    
    
    Text(Point(winWidth/2 - 160, winHeight-350),
                        "Message to code").draw(win)
    keyword = Entry(Point(winWidth/2+45, winHeight-300), 30)
    keyword.setText("")
    keyword.draw(win)
    Text(Point(winWidth/2 - 160, winHeight-300),
                    "Enter Keyword").draw(win)
#wait for the mouse click to continue with encryption
    win.getMouse()
#store the input as a string 
    message1 = str(message.getText())
    keyword1 = str(keyword.getText())

#insert the string input into the encoding method
    string = code(message1, keyword1)
#output the encrypted message to the graphical window
    Text(Point(winWidth/2, winHeight - 120),
         "Encrypted message is:").draw(win)
    output = Text(Point(winWidth/2, winHeight - 90), string)
    output.draw(win)
    instructions.setText("Click to close")


#close the window
    clickPt = win.getMouse()
    win.close()
    
