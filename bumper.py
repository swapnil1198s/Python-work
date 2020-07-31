# Name: Swapnil Srivastava

# bumper.py

# Problem: this program simulates two bumper cars in motion
#       and their collisions with the walls and each other

# Certification of Authenticity:

# I certify that this lab is entirely my own work.



#Import the required libraries
import random
import graphics
from math import sqrt 
from graphics import *

#Method to create a random number and return it
def getRandom(moveAmount):
    num = random.randint(-moveAmount, moveAmount)
    return num

#method to calculate the distance between two points
def calcDistance(point1, point2):
    x1, y1 = point1.getX(), point1.getY()
    x2, y2 = point2.getX(), point2.getY()
    dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist

#Method to check if the two cars have collided
def didCollide(ball, ball2):
    distance = calcDistance(ball, ball2)
    if 40 >= distance:
        return True
    else:
        return False

#method to see if the balls have hit a vertical wall
def hitVertical(ball, win):
#calculate the distance between the wall and the center of the circle
    distance = abs(win - abs(ball.getX()))
#use the distance calculated to determine if the ball has hit a
#   vertical wall
    if 20 >= distance or 580 <= distance:
        print(distance)
        return True
    else:
        print(distance)
        return False
#method to see if the balls have hit a horizontal wall
def hitHorizontal(ball, win):
#calculate the distance between the wall and the center of the circle
    distance = abs(win - abs(ball.getY()))
#use the distance calculated to determine if the ball has hit a
#   horizontal wall
    if 20 >= distance or 380 <= distance:
        print(distance)
        return True
    else:
        print(distance)
        return False
#method to pich and return a random color
def randomColor():
#specify colors in list
    rgbl=["blue", "green", "red"]
#choose color from list
    color = random.choose(rgbl)
    return(color)

def main():
#specify random coordinates
    ranX = getRandom(50)
    ranY = getRandom(10)
    ranX1 = getRandom(50)
    ranY1 = getRandom(10)
#make the window by specifying the width and the height
    winWidth = 600
    winHeight = 400
    win = GraphWin("Bumper cars", winWidth, winHeight)
#make the two circles by specifying the center points and the radii
    center = Point(300,200)
    center2 = Point(360,200)
    radius = int(20)
    ball = Circle(center,radius)
    ball.draw(win)
    ball.setFill("red")
    ball2 = Circle(center2,radius)
    ball2.draw(win)
    ball2.setFill("green")
#check for collision
    checkCollision = didCollide(center, center2)
#loop to move the ball
    for i in range(1000):
#code to move the balls
        ball.move(ranX, ranY)
        ball2.move(ranX1, ranY1)
    #get the new center points after movements
        center = Point(center.getX() + ranX, center.getY() + ranY)
        center2 = Point(center2.getX() + ranX1, center2.getY() + ranY1)
    #if else statements to check for collisions 
        if hitVertical(center, winWidth) == True:
            
            ranX = -ranX
            
        else:
            print("false")
            
        if hitHorizontal(center, winHeight) == True:
            ranY = -ranY
            
        else:
            print("false")
            
        if hitHorizontal(center2, winHeight) == True:
            ranY1 = -ranY1
            
        else:
            print("false")
            
        if hitVertical(center2, winWidth) == True:
            ranX1 = -ranX1
        else:
            print("false")
        if didCollide(center, center2) == True:
            ranX = -ranX
            ranY = -ranY
            ranX1 = -ranX
            ranY1 = -ranY1
        else:
            print("false")
        time.sleep(0.05)

