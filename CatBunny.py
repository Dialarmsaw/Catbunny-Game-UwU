'''
READ ME

Right here is where I am going to be keeping every note for this code.

Time calculation:
at 0 the time is 14:08:12.997704
at 100 the time is 14:08:13.324557

13.324557-12.997704=0.326853

it takes 0.326853 seconds to get to y+100










'''
import turtle
import time
import random
import os
import math
import platform
import winsound
from datetime import datetime
import keyboard #thease are all of the imports that we will need
global caty
global catx
global jumping
global ychange
global gametime
global gravitystrength #thease are the variables we will need to be everywhere
gametime=0
ychange=False
jumping=False
catbunnywin=turtle.Screen() #this creates the window
cbsprite = "/Users/dialarmsaw/mu_code/cbgood.gif"# this registers the sprite of the character
catbunnywin.register_shape(cbsprite)# 
catbunny=turtle.Turtle()            #
catbunny.shape(cbsprite)            #
catbunnywin.bgcolor("purple")       # This is the player turtle
catbunny.penup()                    #
catx=catbunny.xcor()                #
caty=catbunny.ycor()                #

def right():   # This is movement right
    catbunny.setheading(0)
    catbunny.fd(5)

def left(): # This is movement left
    catbunny.setheading(180)
    catbunny.fd(5)

def jump(): # This is the jump
    jumping==True
    catbunny.setheading(90)
    catbunny.fd(100)
def movement():
    if keyboard.is_pressed('d'):
        right()
    if keyboard.is_pressed('a'):
        left()
    if keyboard.is_pressed('space'):
        jump()
def timetojump():
    if jumping==True:
        while ychange!=False:
            playerpos=catbunny.ycor()
            ppot.append(playerpos)
gravitystrength=3 #this defines the gravity
def gravity():
    while not jumping:
        catbunny.dx()-3
ppot=[]  #Player Position Over Time
ppot.append(0)
ppot.append(0)
ppot.append(0)
def changingY():
        if ppot[len(ppot)-1]==catbunny.ycor():
            ychange==False
        else:
            ychange==True
while True: #this is the main game loop
    movement()
    timetojump()
    changingY()
    ppot.append(catbunny.ycor())
    print(catbunny.ycor(),datetime.now())
    gametime+=1
    
    
    
