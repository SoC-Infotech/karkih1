#Import to libraries to our game
import pygame
import random 

#Initializing the pygame (game loop, game scene)
pygame.init()

#Declare some variables/constants
winHeight = 480
winWidth = 700
GREEN =(0,255,0)

#Create window game
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("Hangman by HITESH")

#main program
#create the game lopop to keep the window visible
inplay = True
while inPlay:
    win.fill(GREEN)  #make background colour green
    pygame.display.update()
    pygame.time.delay(100)




#quit thge game
pygame.quit()
