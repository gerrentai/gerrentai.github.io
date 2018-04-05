import pygame
import time
import random

pygame.init()

"""
Tai Gerren/Bailey Hodgin Snake Game 2018.
This game makes use to the PyGame package in Python and uses the arrow keys to control the snake.
This game contains 10 apples, but only one is edible. Every time you eat the safe apple, all apples moves. Eat the wrong one and it's game over.
This verson of the snake game was modified from the tutorial posted by Syntec (from the TheNewBoston.com).
We added comments to represent each item within the code.
"""

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
megagreen = (175,240,30)
niceblue = (66,209,244)
purple = (125, 0, 255)
cyan = (66, 235, 244)
nicepurple =(208, 165, 209)
apple = (50, 160, 50)
ded = (30, 140, 30)

#window size
display_width = 1200
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snack')

#refresh rate
clock = pygame.time.Clock()
FPS = 300

#block size / snake size
block_size = 10

font = pygame.font.SysFont(None, 25)

def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, purple, [XnY[0], XnY[1], block_size, block_size])

def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    #apple
    randAppleX = round (random.randrange(0, display_width-block_size))
    randAppleY = round (random.randrange(0, display_height-block_size))

    #poison apples
    randApple2X = round (random.randrange(0, display_width-block_size))
    randApple2Y = round (random.randrange(0, display_height-block_size))
    randApple3X = round (random.randrange(0, display_width-block_size))
    randApple3Y = round (random.randrange(0, display_height-block_size))
    randApple4X = round (random.randrange(0, display_width-block_size))
    randApple4Y = round (random.randrange(0, display_height-block_size))
    randApple5X = round (random.randrange(0, display_width-block_size))
    randApple5Y = round (random.randrange(0, display_height-block_size))
    randApple6X = round (random.randrange(0, display_width-block_size))
    randApple6Y = round (random.randrange(0, display_height-block_size))
    randApple7X = round (random.randrange(0, display_width-block_size))
    randApple7Y = round (random.randrange(0, display_height-block_size))
    randApple8X = round (random.randrange(0, display_width-block_size))
    randApple8Y = round (random.randrange(0, display_height-block_size))
    randApple9X = round (random.randrange(0, display_width-block_size))
    randApple9Y = round (random.randrange(0, display_height-block_size))
    randApple10X = round (random.randrange(0, display_width-block_size))
    randApple10Y = round (random.randrange(0, display_height-block_size))

    while not gameExit:

        #death screen
        while gameOver == True:
            gameDisplay.fill(niceblue)
            message_to_screen("You ded, press C to ded again or Q to give up", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #movement/speed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -1
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 1
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -1
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 1
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(niceblue)

        #good apple
        AppleThickness = 20
        pygame.draw.rect(gameDisplay, apple, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        #all bad apples are slightly different to the good one
        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple2X, randApple2Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple3X, randApple3Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple4X, randApple4Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple5X, randApple5Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple6X, randApple6Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple7X, randApple7Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple8X, randApple8Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple9X, randApple9Y, AppleThickness, AppleThickness])

        AppleThickness = 21
        pygame.draw.rect(gameDisplay, ded, [randApple10X, randApple10Y, AppleThickness, AppleThickness])

        #snake head
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()

        #eating good apple
        if lead_x >= randAppleX and lead_x <=randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
               randAppleX = round (random.randrange(0, display_width-block_size))
               randAppleY = round (random.randrange(0, display_height-block_size))
               randApple2X = round (random.randrange(0, display_width-block_size))
               randApple2Y = round (random.randrange(0, display_height-block_size))
               randApple3X = round (random.randrange(0, display_width-block_size))
               randApple3Y = round (random.randrange(0, display_height-block_size))
               randApple4X = round (random.randrange(0, display_width-block_size))
               randApple4Y = round (random.randrange(0, display_height-block_size))
               randApple5X = round (random.randrange(0, display_width-block_size))
               randApple5Y = round (random.randrange(0, display_height-block_size))
               randApple6X = round (random.randrange(0, display_width-block_size))
               randApple6Y = round (random.randrange(0, display_height-block_size))
               randApple7X = round (random.randrange(0, display_width-block_size))
               randApple7Y = round (random.randrange(0, display_height-block_size))
               randApple8X = round (random.randrange(0, display_width-block_size))
               randApple8Y = round (random.randrange(0, display_height-block_size))
               randApple9X = round (random.randrange(0, display_width-block_size))
               randApple9Y = round (random.randrange(0, display_height-block_size))
               randApple10X = round (random.randrange(0, display_width-block_size))
               randApple10Y = round (random.randrange(0, display_height-block_size))
               snakeLength += 15

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
               randAppleX = round (random.randrange(0, display_width-block_size))
               randAppleY = round (random.randrange(0, display_height-block_size))
               randApple2X = round (random.randrange(0, display_width-block_size))
               randApple2Y = round (random.randrange(0, display_height-block_size))
               randApple3X = round (random.randrange(0, display_width-block_size))
               randApple3Y = round (random.randrange(0, display_height-block_size))
               randApple4X = round (random.randrange(0, display_width-block_size))
               randApple4Y = round (random.randrange(0, display_height-block_size))
               randApple5X = round (random.randrange(0, display_width-block_size))
               randApple5Y = round (random.randrange(0, display_height-block_size))
               randApple6X = round (random.randrange(0, display_width-block_size))
               randApple6Y = round (random.randrange(0, display_height-block_size))
               randApple7X = round (random.randrange(0, display_width-block_size))
               randApple7Y = round (random.randrange(0, display_height-block_size))
               randApple8X = round (random.randrange(0, display_width-block_size))
               randApple8Y = round (random.randrange(0, display_height-block_size))
               randApple9X = round (random.randrange(0, display_width-block_size))
               randApple9Y = round (random.randrange(0, display_height-block_size))
               randApple10X = round (random.randrange(0, display_width-block_size))
               randApple10Y = round (random.randrange(0, display_height-block_size))
               snakeLength += 15

        #eating poisonous apples
        if lead_x >= randApple2X and lead_x <=randApple2X + AppleThickness or lead_x + block_size > randApple2X and lead_x + block_size < randApple2X + AppleThickness:
            if lead_y > randApple2Y and lead_y < randApple2Y + AppleThickness:
               randApple2X = round (random.randrange(0, display_width-block_size))
               randApple2Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple2Y and lead_y + block_size < randApple2Y + AppleThickness:
                randApple2X = round (random.randrange(0, display_width-block_size))
                randApple2Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple3X and lead_x <=randApple3X + AppleThickness or lead_x + block_size > randApple3X and lead_x + block_size < randApple3X + AppleThickness:
            if lead_y > randApple3Y and lead_y < randApple3Y + AppleThickness:
               randApple3X = round (random.randrange(0, display_width-block_size))
               randApple3Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple3Y and lead_y +block_size < randApple3Y + AppleThickness:
                randApple3X = round (random.randrange(0, display_width-block_size))
                randApple3Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple4X and lead_x <=randApple4X + AppleThickness or lead_x + block_size > randApple4X and lead_x + block_size < randApple4X + AppleThickness:
            if lead_y > randApple4Y and lead_y < randApple4Y + AppleThickness:
               randApple4X = round (random.randrange(0, display_width-block_size))
               randApple4Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple4Y and lead_y + block_size < randApple4Y + AppleThickness:
                randApple4X = round (random.randrange(0, display_width-block_size))
                randApple4Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple5X and lead_x <=randApple5X + AppleThickness or lead_x + block_size > randApple5X and lead_x + block_size < randApple5X + AppleThickness:
            if lead_y > randApple5Y and lead_y < randApple5Y + AppleThickness:
               randApple5X = round (random.randrange(0, display_width-block_size))
               randApple5Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple5Y and lead_y + block_size < randApple5Y + AppleThickness:
                randApple5X = round (random.randrange(0, display_width-block_size))
                randApple5Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple6X and lead_x <=randApple6X + AppleThickness or lead_x + block_size > randApple6X and lead_x + block_size < randApple6X + AppleThickness:
            if lead_y > randApple6Y and lead_y < randApple6Y + AppleThickness:
               randApple6X = round (random.randrange(0, display_width-block_size))
               randApple6Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple6Y and lead_y + block_size < randApple6Y + AppleThickness:
                randApple6X = round (random.randrange(0, display_width-block_size))
                randApple6Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple7X and lead_x <=randApple7X + AppleThickness or lead_x + block_size > randApple7X and lead_x + block_size < randApple7X + AppleThickness:
            if lead_y > randApple7Y and lead_y < randApple7Y + AppleThickness:
               randApple7X = round (random.randrange(0, display_width-block_size))
               randApple7Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple7Y and lead_y + block_size < randApple7Y + AppleThickness:
                randApple7X = round (random.randrange(0, display_width-block_size))
                randApple7Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple8X and lead_x <=randApple8X +AppleThickness or lead_x + block_size > randApple8X and lead_x + block_size < randApple8X + AppleThickness:
            if lead_y > randApple8Y and lead_y < randApple8Y + AppleThickness:
               randApple8X = round (random.randrange(0, display_width-block_size))
               randApple8Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple8Y and lead_y + block_size < randApple8Y + AppleThickness:
                randApple8X = round (random.randrange(0, display_width-block_size))
                randApple8Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple9X and lead_x <=randApple9X + AppleThickness or lead_x + block_size > randApple9X and lead_x + block_size < randApple9X + AppleThickness:
            if lead_y > randApple9Y and lead_y < randApple9Y + AppleThickness:
               randApple9X = round (random.randrange(0, display_width-block_size))
               randApple9Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple9Y and lead_y + block_size < randApple9Y + AppleThickness:
                randApple9X = round (random.randrange(0, display_width-block_size))
                randApple9Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        if lead_x >= randApple10X and lead_x <=randApple10X + AppleThickness or lead_x + block_size > randApple10X and lead_x + block_size < randApple10X + AppleThickness:
            if lead_y > randApple10Y and lead_y < randApple10Y + AppleThickness:
               randApple10X = round (random.randrange(0, display_width-block_size))
               randApple10Y = round (random.randrange(0, display_height-block_size))
               gameOver = True

            elif lead_y + block_size > randApple10Y and lead_y + block_size < randApple10Y + AppleThickness:
                randApple10X = round (random.randrange(0, display_width-block_size))
                randApple10Y = round (random.randrange(0, display_height-block_size))
                gameOver = True

        #refresh rate
        clock.tick(FPS)

    #game exit
    pygame.quit()
    quit()

#keep window open
gameLoop()
