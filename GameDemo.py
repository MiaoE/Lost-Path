
"""
Lost Path.py
Derron Li | Eric Miao
May 23, 2019~June 12, 2019
"""

# Import necessities
import pygame
import os, sys
import math, time
from random import randint
from pygame.locals import *
from pygame.constants import *

# Initialize pygame
pygame.init()

# Initiate colour variables
WHITE = 255, 255, 255
BLACK = 0, 0, 0
GREY = 124, 124, 124
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
SKY = 0, 215, 255
PINK = 245, 0, 175
CYAN = 0, 200, 255

# Initiate gamewindow platform
WIDTH = 1000
HEIGHT = 700
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF)

# Class of GRIDS for positioning assist purpose
class grid:
    def __init__(self, color):
        self.color = color

    def gridall(self):
        for x in range(0, WIDTH, 10):
            if x % 100 != 0:
                pygame.draw.line(gameWindow, self.color, (x, 0), (x, HEIGHT), 1)
            else:
                pygame.draw.line(gameWindow, self.color, (x, 0), (x, HEIGHT), 2)
            # end if
        # end for loop
        for y in range(0, HEIGHT, 10):
            if y % 100 != 0:
                pygame.draw.line(gameWindow, self.color, (0, y), (WIDTH, y), 1)
            else:
                pygame.draw.line(gameWindow, self.color, (0, y), (WIDTH, y), 2)
            # end if
        # end for loop

# Initiate different backgrounds and background music
class background:
    def __init__(self, color):
        #Background images
        if color == 1:
            picture = pygame.image.load("inGame1.jpg").convert_alpha()
            gameWindow.blit(picture, (0, 0))
        elif color == "title":
            picture = pygame.image.load("titleScreen.jpg").convert_alpha()
            gameWindow.blit(picture, (0, 0))
        elif color == "main":
            picture = pygame.image.load("MainMenu.png").convert_alpha()
            gameWindow.blit(picture, (0, 0))
        elif color == "tut":
            picture = pygame.image.load("TUTORIAL.jpg").convert_alpha()
            gameWindow.blit(picture, (0, 0))
        #Names of files are accurate descriptions of what the image is
        #Some are given number values so they can be easily changed, while still in game
        elif color == 2:
            picture = pygame.image.load("CITY.jpg").convert_alpha()
            gameWindow.blit(picture, (0, 0))
        elif color == 3:
            picture = pygame.image.load("Fantasy.jpg").convert_alpha()
            gameWindow.blit(picture, (0,0))
        elif color == "soon":
            picture = pygame.image.load("COMING SOON.jpg").convert_alpha()
            gameWindow.blit(picture, (0,0))
        elif color == "complete":
            picture = pygame.image.load("WINGAME.jpg").convert_alpha()
            gameWindow.blit(picture, (0,0))
        #All background music here
        elif color == 4:
            pygame.mixer.music.load("CalmMusic.mp3")
            pygame.mixer.music.play(-1)
        elif color == 5:
            pygame.mixer.music.load("BETTER.mp3")
            pygame.mixer.music.play(-1)
        elif color == 6:
            pygame.mixer.music.load("EPIC5.mp3")
            pygame.mixer.music.play(-1)
        else: 
            gameWindow.fill(color)
            #v = grid(BLACK)
            #v.gridall()       
        # end if

# Initiate exit function
def exit():
    print ("exit successful")
    pygame.quit()
    sys.exit(0)

# Define fail screen
def fail():
    global running, health, dead, menu, back
    #gloabalizes variables so they can be used throughout the code
    #Sets backbground as variable back (value of 1) so it can be changed later
    background(back)
    # initiate texts variables
    font2 = pygame.font.SysFont("Times New Roman", 30)
    urd = font2.render("YOU ARE DEAD", 0, RED)
    tryagain = font2.render("Try Again?", 0, RED)
    yes = font2.render("YES", 0, GREEN)
    yes1 = font2.render("YES", 0, GREY)
    no = font2.render("NO", 0, RED)
    no1 = font2.render("NO", 0, GREY)
    gameWindow.blit(urd, (400, 25))

    answered = False
    pygame.display.update()
    pygame.time.delay(1000)
    gameWindow.blit(tryagain, (450, 300))

    # while loop
    while not answered:
        #Displays drawings and texts of option(dead) menu
        pygame.draw.rect(gameWindow, BLUE, (420, 350, 80, 50))
        pygame.draw.rect(gameWindow, BLUE, (540, 350, 80, 50))
        gameWindow.blit(yes, (430, 358))
        gameWindow.blit(no, (560, 358))
        pygame.display.update()
        # get the position of the mouse
        mouseX, mouseY = pygame.mouse.get_pos()
        # for loop - detects any movement/actions on computer hardwares
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # end if
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Try again: Yes
                if mouseX > 420 and mouseX < 500 and mouseY > 350 and mouseY < 400:
                    #Resets the music to the beginning one
                    background(4) #When the user plays try again, they will have to start from the beginning
                    print ("PLAY AGAIN AFFIRMATIVE")
                    answered = True
                    health = 10
                    dead = False
                    menu = True
                    #resets required variables so game can continue
                #Try again: No
                elif mouseX > 540 and mouseX < 620 and mouseY > 350 and mouseY < 400:
                    gameWindow.blit(no1, (700, 300))
                    print ("PLAY AGAIN NEGATIVE")
                    answered = True
                    running = False
                    # when running = False, the main program while loop breaks, 
                    # directing to exit()
                    # end inner if
               # end outer if
        # end for loop
    #end while loop

# Class to draw a meteor
class meteoroid:
    # initiate image variable
    meteor = pygame.image.load("Meteor2.png").convert_alpha()
 
    def __init__(self):
        self.meteor = pygame.transform.scale(self.meteor, (84, 93))
 
    def meteoroid_draw(self, x, y):
        # sets a variable as image, only update that image's location
        w = gameWindow.blit(self.meteor, (x, y))
        pygame.display.update(w)
 
# Class to draw the character
class character:
    # initiate variable before using them in functions in the class
    x = 0
    y = 0
    c = pygame.image.load("Character Stand.png").convert_alpha()

    def __init__(self, sizeX, sizeY, position):
        self.x = sizeX
        self.y = sizeY
        self.position = position
        self.c = pygame.transform.scale(self.c, (self.x, self.y))
        self.c = gameWindow.blit(self.c, self.position)
        pygame.display.update()

# Initiate health bar function
def heart(health):
    # initiate image variables
    heart = pygame.image.load("Heart.png").convert_alpha()
    heartImage = pygame.transform.scale(heart, (45, 45))
    if health == 5:
        #Displays all hearts along top left of screen
        gameWindow.blit(heartImage, (30, 15))
        gameWindow.blit(heartImage, (55, 15))
        gameWindow.blit(heartImage, (80, 15))
        gameWindow.blit(heartImage, (105, 15))
        gameWindow.blit(heartImage, (130, 15))
    elif health == 4:
        gameWindow.blit(heartImage, (30, 15))
        gameWindow.blit(heartImage, (55, 15))
        gameWindow.blit(heartImage, (80, 15))
        gameWindow.blit(heartImage, (105, 15))
    elif health == 3:
        gameWindow.blit(heartImage, (30, 15))
        gameWindow.blit(heartImage, (55, 15))
        gameWindow.blit(heartImage, (80, 15))
    elif health == 2:
        gameWindow.blit(heartImage, (30, 15))
        gameWindow.blit(heartImage, (55, 15))
    elif health == 1:
        gameWindow.blit(heartImage, (30, 15))
    # end if
# Class for the position of the characters, using draw character function to draw
class player:
    oneX = 0
    oneY = 0

    def __init__(self, x, y):
        self.oneX = x
        self.oneY = y
 
    def getX(self):
        return self.oneX
 
    def getY(self):
        return self.oneY
 
    def setX(self, val):
        self.oneX = val
 
    def setY(self, val):
        self.oneY = val
 
    def left(self, val):
        self.oneX -= val
        return self.oneX
 
    def right(self, val):
        self.oneX += val
        return self.oneX

    def display(self, number):
        clock = pygame.time.Clock()
        pos = (self.oneX, self.oneY)
        character(300, 300, pos)
        self.size = number
        clock.tick(2000)
 
# Class for the position of the meteor + function to draw the meteor
class meteoroid_array:
    # initiate variables
    meteoroid_array_x = []
    meteoroid_array_y = []
    size = 0

    def __init__(self, number, x, y):
        self.size = number
        self.meteoroid_array_x = x
        self.meteoroid_array_y = y
 
    def getX(self, index):
        if index < self.size:
            return self.meteoroid_array_x[index]
 
    def getY(self, index):
        if index < self.size:
            return self.meteoroid_array_y[index]
 
    def setX(self, index, value):
        if index < self.size:
            self.meteoroid_array_x[index] = value
 
    def setY(self, index, value):
        if index < self.size:
            self.meteoroid_array_y[index] = value
 
    def meteoroid_array_draw(self, x, y, w):
        clock = pygame.time.Clock()
        for i in range(self.size):
            rects = meteoroid()
            rects.meteoroid_draw(self.meteoroid_array_x[i], self.meteoroid_array_y[i])
            pygame.draw.rect(gameWindow, BLACK, (x, y, w, 10))  
            # pygame.display.update(rects)
        # end for loop
        
        # as more meteors, the game runs the loop more times, takes longer
        # the clock tick is for balancing the FPS
        if self.size < 4:
            clock.tick(450)
        elif self.size < 5:
            clock.tick(460)
        elif self.size < 6:
            clock.tick(550)
        elif self.size < 7:
            clock.tick(600)
        elif self.size < 8:
            clock.tick(660)
        elif self.size < 9:
            clock.tick(720)
        elif self.size < 11:
            clock.tick(750)
        elif self.size < 12:
            clock.tick(880)
        elif self.size < 13:
            clock.tick(920)
        else:
            clock.tick(950)
        # end if
# Initiate function for the giant diagonal meteor
def bigThing():
     global bigSize, bigPosX, bigPosY
     met = pygame.image.load("Meteor1.png").convert_alpha()
     bigMet = pygame.transform.scale(met, (bigSize,bigSize))
     gameWindow.blit(bigMet,(bigPosX, bigPosY))

# Initiate main action pack of function
def meteoroid_action():
    # initiate variables used/edited outside of the function
    global health, dead, bigSize, bigPosX, bigPosY, back, win, music
    # initiate variables
    back = 1
    bigPosX = 1010
    bigPosY = -7
    music = 4
    count = 3 # max 12, number of meteors
    font3 = pygame.font.SysFont("Arial", 32)
    # initialiate lists for positions
    meteoroid_action.x = []  
    meteoroid_action.y = []
    # --------------------- all movement variables
    velocity = 0 #speed of character
    fall = False
    jump = False  # type: bool
    hit = 0 #Timer after being hit
    bigSpeedX = 0
    bigSpeedY = 0 #Speed of big diagonal meteor
    hard = 0 #once count(# of meteors) becomes 12, hard mode is initiated
    #Creates random x and y positions for the platform and the character
    xPosStart = randint(50, 400)
    yPosStart = randint(500, 600)
    xLength = randint(300, 500)
    xPosEnd = xPosStart + xLength
    # sets the timer for levels of difficulty
    timer = 500
    # initialize initial speed for meteors
    speed = 15

    # done with initializing variables, checking to make sure it runs
    print (count, "meteoroids")
    
    # creating object locations
    for i in range(count):  
        # Gets random x and y positions for the meteors and saves to list
        meteoroid_action.x.append(randint(0, WIDTH - 30))  
        meteoroid_action.y.append(randint(-1500, -30))
    # end for loop
    # saving all meteors as one object/variable
    ob = meteoroid_array(count, meteoroid_action.x, meteoroid_action.y)
    # initializing player starting position and variable name for future use
    starting = player(xPosStart + xLength/2, yPosStart-125)
    starting.display(count)

    heart(health)
    # main while loop
    while health >= 1:
        count = count
        # checks for the level
        if count==6 and back<2: #The back<2 makes it so these if statements can only run through once
           #Adds to back(changes background), music (changes song), plays new song
            back +=1
            music +=1
            background(music)
        #Scene(level) change once again
        elif count ==10 and back<3:
            back+=1
            music+=1
            background(music)
        #We programmed maximum of 3 hard mode levels
        #So once hard becomes 4, the player has won.
        elif count == 12 and hard==4:
            win = True 
            health = 0 # breaks out of loop direct to win screen
            print ("win", win)
       # end if
        
        background(back)
        # timer always runs
        timer -= 1
        # if player survives until timer reaches 0, one more meteor added (increase difficulty)
        if timer <= 1:
            if count <12:
                count += 1
                # add in one more position to the list
                meteoroid_action.x.append(randint(0, WIDTH - 30))  
                meteoroid_action.y.append(randint(-1500, -30))
                # resets the variable so it is updated
                ob = meteoroid_array(count, meteoroid_action.x, meteoroid_action.y)
            else:
                #If number of meteors is 12, it will not add anymore
                #instead it will add 1 to hard, bringing player to hard mode levels
                hard+=1
             # end inner if
            # always resets the timer
            timer = 500
            # for us to know it came to this step
            print ("harder")
            print (count, "meteoroids")
        # as more difficult, big meteor appears more frequently (function in this block)
        # end outer if
        if count==3:
            #Lowers range of random number (increases changes of rolling 30)
            #This also increases the chance of the number rolling twice or more times in a row. This will lead to the meteor appearing from one positon, and then going to a different one
            #This is essentially the meteor tricking the player
            #Contrary to popular belief: This is in fact a function of the game
            big = randint(0,500)
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -3
                bigSpeedY = 3
                # end if
        elif count ==4:
            big = randint(0,400)
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -3
                bigSpeedY = 3
                # end if
        elif count==5:
            big = randint(0,300)
            speed= 16
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4 #Also increases speed of big meteor overtime
                # end if
                
        elif count==6:
            big = randint(0,300)
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4
                # end if
        elif count==7:
            big = randint(0,300)
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4
                # end if
        elif count==8:
            big = randint(0,200)
            speed = 20 #Increases speed of regular meteors
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4
                # end if
                
        elif count==9:
            big = randint(0,200)
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4
                # end if
        elif count==10:
            big = randint(0,200)
            speed= 22
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4
            # end if
        elif count==11:
            big = randint(0,150)
            speed=23
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4
            # end if

        elif count==12:
            big = randint(0,125)
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -4
                bigSpeedY = 4
            # end if
        elif hard ==1: #Hard mode levels
            big = randint(0,125)
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -5
                bigSpeedY = 5
            # end if
        elif hard ==2:
            big = randint(0,100)
            speed=28
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -5
                bigSpeedY = 5
            # end if
                
        elif hard ==3:
            big = randint(0,75)
            speed=30
            if big == 30:
                bigPosX = randint(700,1300)
                bigPosY = -7
                bigSpeedX = -6
                bigSpeedY = 6
            # end if
        # end outer if
        # end block for frequency of big meteor

        # resets all meteor position movement by one (for loop)
        for m in range(count): 
            bigPosX += bigSpeedX
            bigPosY += bigSpeedY
            #Increases position of big meteor by the speed
            bigThing()
            #Draws big meteor
            heart(health)
            #Changes position of the smaller meteors by the speed
            ob.setY(m, ob.getY(m) + speed)
            #draws smaller meteors
            ob.meteoroid_array_draw(xPosStart, yPosStart, xLength)
            starting.display(count)

            # collision block for small meteor and bigger diagonal one
            if hit == 0:
                #top left corner collision 
                if ((starting.getX() + 20 <= ob.getX(m) + 23 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= ob.getY(m) + 13 <= starting.getY() + 118)) or ((starting.getX() + 20 <= bigPosX + 10 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= bigPosY + 10 <= starting.getY() + 118)):
                    health -= 1
                    hit = 100
                    #Minuses one health and makes hit 100
                    #This is a number timer, so that the player cannot be hit multiple times in a row
 
                    pygame.time.delay(500)
                #top right corner collision
                elif (starting.getX() + 20 <= ob.getX(m) + 23 + 35 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= ob.getY(m) + 13 <= starting.getY() + 118) or (starting.getX() + 20 <= bigPosX+10+80 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= bigPosY +10 <= starting.getY() + 118):
                    health -= 1
                    hit = 100
                    #Delays code for a short time so user can see how and where they got hit
                    pygame.time.delay(500)
                #bottom left corner
                elif (starting.getX() + 20 <= ob.getX(m) + 23 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= ob.getY(m) + 13 + 67 <= starting.getY() + 118) or (starting.getX() + 20 <= bigPosX+10 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= bigPosY +10+80 <= starting.getY() + 118):
                    health -= 1
                    hit = 100
 
                    pygame.time.delay(500)
                #bottome right corner
                elif (starting.getX() + 20 <= ob.getX(m) + 23 + 35 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= ob.getY(m) + 13 + 67 <= starting.getY() + 118) or (starting.getX() + 20 <= bigPosX +10+80 <= starting.getX() + 68) and (
                        starting.getY() + 10 <= bigPosY+10+80 <= starting.getY() + 118) :
                    health -= 1
                    hit = 100
 
                    pygame.time.delay(500)
                # end if
            # end if
            # end collision block

            # hit is the timer for invincibility
            # once hit=0, player is not invincible
            hit -= 1
            if hit < 0:
                hit = 0
            # end if

            # Reset the position of that meteor when it reaches bottom
            if ob.getY(m) >= 700:  
                ob.setX(m, randint(0, WIDTH - 30))
                ob.setY(m, randint(-1500, -100))
            # end if
        # end for loop
        
        # character moving action (block)
        pygame.event.get()
        key = pygame.key.get_pressed()
        if pygame.KEYDOWN:
            #use arrows or a and d to move character
            if (key[pygame.K_LEFT] or key[pygame.K_a]):  # and starting.getX() > 130:
                starting.setX(starting.getX() -15)
            # end if
            if (key[pygame.K_RIGHT] or key[pygame.K_d]):  # and starting.getX() < 570:
                starting.setX(starting.getX() + 15)
            #Use space to jump
            # end if
            if key[pygame.K_SPACE]:
                #Will only allow jump if character is on the platform
                if starting.getY() == yPosStart-125 and not (starting.getX() < xPosStart-75 or starting.getX() > xPosEnd-30):
                    #sets velocity to a negative value
                    velocity = JUMPSPEED
                    jump = True
                # end if
            # end if
        # end if
        #if character is on platform
        if starting.getX() > xPosStart-75 and starting.getX() < xPosEnd-30 and not jump and not fall:
            velocity = 0
        # end if
        #If character is falling
        if (starting.getX() < xPosStart-75 or starting.getX() > xPosEnd-30) and starting.getY() > yPosStart-125:
            fall = True
        # end if
        #if y position is past height of the screen, lose health and respawn at top of platform
        if starting.getY() > HEIGHT:
            health -= 1
            starting.setX(xPosStart + xLength/2)
            starting.setY(yPosStart-125)
            hit = 200 #Once respawned, the hit timer starts again, so player will not be hit as soon as being respawn
            fall = False
        # end if
        #Increases velocity from a negative to a positive (up and down)
        velocity += 4
        #Changes position of character by velocity
        starting.setY(starting.getY() + velocity)
 
        if starting.getY() >= yPosStart-125 and starting.getX() > xPosStart-75 and starting.getX() < xPosEnd-30 and not fall:
            starting.setY(yPosStart-125)
            jump = False
        # end moving block
        # end if
    # end while loop (main loop in function) (when health < 1)
    dead = True
    
# Initiate menu screen function
def mainMenu():
    global start, tutorial, campaign
    #while loop for the mode the user wants
    while not start:
        #different background
        background("main")
        pygame.display.update()
        mouseX, mouseY = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # end if
            if event.type == pygame.MOUSEBUTTONDOWN:
                #if mouse click is within the range of the box
                if (350 < mouseX < 680) and (200 < mouseY < 270):
                    campaign = True
                    start = True
                    print ("campaign")
                # end if
                if (350 < mouseX < 680) and (300 < mouseY < 370):
                    tutorial = True
                    start = True
                    print ("tutorial")
                # end if
                if (280 < mouseX < 720) and (365 < mouseY < 440):
                    background("soon")
                    pygame.display.update()
                    pygame.time.delay(2000)
                # end if
                if (415 < mouseX < 580) and (450 < mouseY < 510):
                    exit()
                # end if
            # end if
    # end while loop
                  
# Initiate tutorial function
def tutor():
    global start, tutorial
    # while loop for when the user wants to see the tutorial (instructions)
    while tutorial:
        background("tut")
        pygame.display.update()
        pygame.event.get()
        keys = pygame.key.get_pressed()
        #Backspace will set tutorial as false(returning back to the menu)
        if keys[pygame.K_BACKSPACE]:
            tutorial = False
            start = False
        # end if
    # end while loop

# Initiate title page function
def title():
    global play, music
    # while loop
    while not play:
        background("title")
        pygame.display.update()
        mouseX, mouseY = pygame.mouse.get_pos()
        # for loop for actions
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # end if
            if event.type == pygame.MOUSEBUTTONDOWN:
            # when the user wants to play
                if (800 < mouseX < 970) and (620 < mouseY < 680):
                    play = True
                # end if
            # end if
        # end for loop
    # end while loop
 
# Initiate winner screen function
def winner():
    global win, start
    # while loop for win
    while win:
        background("complete")
        pygame.display.update()
        pygame.event.get()
        key = pygame.key.get_pressed()
        #If space is pressed, user will exit from program
        if key[pygame.K_SPACE]:
            exit()
        # end if
    # end while loop

# Initiate username screen for campaign mode
def setup():
    global menu, finishSetup, back
    font = pygame.font.Font(None, 32)
    font1 = pygame.font.SysFont("Arial", 32)
    # welcome message / input username
    usernameMessage = "Welcome to Lost Path, please enter your username"
    setup.username = ''
    usernameMessage = font1.render(usernameMessage, 0, RED)
    # while loop for set ups
    while not finishSetup:
        # for loop for action detections
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # end if
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # enters the final username
                    finishSetup = True
                    menu = True
                elif event.key == K_BACKSPACE:
                    # delete the last character of the String
                    setup.username = setup.username[:-1]
                    # print username
                else:
                    # adds the character to the String
                    setup.username += event.unicode
                    # print username
                # end if
            # end if
        # end for loop (always updating what's on the String)
        background(back)
        gameWindow.blit(usernameMessage, (100, 265))
        textSurface = font.render(setup.username, True, BLACK)
        gameWindow.blit(textSurface, (100, 300))
 
        pygame.display.update()
    # end while loop

# Main program starts here------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# RUNNING BOOLEAN
running = True

# INITIATING VARIABLES AND OTHER BOOLEANS
start = False
menu = True
dead = False
finishSetup = False
level = 0
limit = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
tutorial = False
campaign = False
play = False
back = 1
win = False
JUMPSPEED = -35
bigSize = 100
bigPosX = 1010
bigPosY = -7
music = 4

#Starts playing music from the very beginning
#Not placed within the while loop because that will lead to constant replaying of music 
background(music)
# MAIN WHILE LOOP
while running:
    # TITLE SCREEN, WAIT UNTIL USER CLICK PLAY OR X TO EXIT
    title()
    # MENU SCREEN WITH FOUR OPTIONS
    mainMenu()
    # INITIATE HEALTH
    health = 5
    # TUTORIAL
    # IF TUTOR IN MENU IS FALSE, THIS FUNCTION BREAKS, WON'T RUN
    tutor()
    # CAMPAIGN MODE
    if start:
        # USERNAME
        setup()
        print ("Your username has been set to:", setup.username)
        # LOOP WHEN NOT DEAD IN ACTION PACK
        if not dead:
           background(back)
           pygame.display.update()
           print ("back to this screen")
           meteoroid_action()
        # WHEN DEAD, TWO OUTCOMES POSSIBLE - WON OR DIED
        else:
            if win:
                # winner screen
                winner()
            else:
                print ("dead")
                # mission failed
                fail()
        # end if
    # end if
# end while
# GAME FINISHED, NOT RUNNING
exit()





