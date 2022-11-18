import pygame
import sys
from pygame.locals import *
import time
import random
from window import Window
from paddle import Paddle
from ball import Ball
from blocks import Blocks



level = 1
lives = 3

def breakout():
    global level,lives
    #Refresh rate
    fps = 60
    fpsclock=pygame.time.Clock()

    #Classes to draw
    window = Window()
    paddle = Paddle(window.screen)
    ball = Ball(window.screen)
    blocks = Blocks(window.screen)
    #Levels
    if level == 1:
        blockslist = blocks.create_blocks(window.screen)
    elif level ==2:
        blockslist = blocks.create_blocks2(window.screen)
    elif level ==3:
        blockslist = blocks.create_blocks3(window.screen)
    else:
        blockslist = blocks.create_blocks4(window.screen)
    #GameLoop
    while window.running:

    #Exit window on escape
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.running = False
                return True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    window.running = False
                    return True

    #Get keys pressed
        key_input = pygame.key.get_pressed()
    #Move paddle left & right
        if key_input[pygame.K_LEFT] and paddle.xposition>0:
            paddle.xposition -= 10
            paddle.move(window.screen)

        if key_input[pygame.K_RIGHT] and paddle.xposition<1000:
            paddle.xposition += 10
            paddle.move(window.screen)
    #Check collision
        ball.check_paddle_collision(window.screen,paddle.paddle,blockslist)
    #Moving Ball
        ball.move_ball(window.screen,paddle.paddle)
    #Check to see if ball is still live if not restart
        if ball.restart_ball(window.screen):
            lives-=1

    #End game loop when lives = 0
        if lives == 0:
            break
    #Checks to see if board was cleared
        if blocks.board_cleared(blockslist):
            level+=1
            break
    #Display lives
        blocks.display_lives(window.screen,lives)
    #Display level
        blocks.display_level(window.screen,level)

    #Allows us to set a refreh rate
        fpsclock.tick(fps)

def restart_game():
    global lives,level
    window2 = Window()

    restart = False

    fps = 60
    fpsclock=pygame.time.Clock()
#Text on screen
    font = pygame.font.SysFont(None, 24)
    img = font.render('Press the "Space Bar" to Play Again press "esc" to exit!', True, "white")
    rect_boundry = pygame.draw.rect(window2.screen, "black", pygame.Rect(400, 400, 200, 20))

    while window2.running:

        window2.screen.blit(img, rect_boundry)
        pygame.display.update()
        window2.screen.fill("black")

# Exit window on escape
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window2.running = False
                return False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    window2.running = False
                    return False
                elif event.key == K_SPACE:
                    lives = 3
                    level =1
                    window2.running = False
                    rect_boundry = pygame.draw.rect(window2.screen, "white", pygame.Rect(-600, 200, 0, 0))
                    pygame.display.update()
                    time.sleep(2)
                    return True

        fpsclock.tick(fps)

def start_game():
    while True:
        if breakout():
            break
        if breakout():
            break
        if breakout():
            break
        if breakout():
            break
        time.sleep(2)
        if restart_game() == True:
            start_game()
        else:
            break

start_game()




