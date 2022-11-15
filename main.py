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

def breakout():
    global level
    #Refresh rate
    fps = 60
    fpsclock=pygame.time.Clock()

    #Classes to draw
    window = Window()
    paddle = Paddle(window.screen)
    ball = Ball(window.screen)
    blocks = Blocks(window.screen)
    if level == 1:
        blockslist = blocks.create_blocks(window.screen)
    else:
        blockslist = blocks.create_blocks2(window.screen)
    #GameLoop
    while window.running:

    #Exit window on escape
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.running = False

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
        ball.move_ball(window.screen)
    #Check to see if ball is still live if not restart
        ball.restart_ball(window.screen)
    #Checks to see if board was cleared
        if blocks.board_cleared(blockslist):
            level=2
            blocks.level+=1
            break

    #Allows us to set a refreh rate
        fpsclock.tick(fps)

breakout()
breakout()


