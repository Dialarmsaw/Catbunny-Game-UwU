import turtle
import time
import random
import os
import math
import platform
import winsound
import keyboard #thease are all of the imports that we will need
global caty
global catx
global jumping
global gravitystrength #thease are the variables we will need to be everywhere
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
    catbunny.setheading(90)
    catbunny.fd(100)
    jumping=True
def movement():
    if keyboard.is_pressed('d'):
        right()
    if keyboard.is_pressed('a'):
        left()
    if keyboard.is_pressed('space'):
        jump()
gravitystrength=3 #this defines the gravity
def gravity():
    while not jumping:
        catbunny.dx()-3


while True: #this is the main game loop
    movement()
    
    
    
