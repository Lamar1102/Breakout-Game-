import pygame
import sys
from pygame.locals import *
import time
import random
from window import Window
from paddle import Paddle
from ball import Ball
from blocks import Blocks

#Refresh rate
fps = 60
fpsclock=pygame.time.Clock()

#Classes to draw
window = Window()
paddle = Paddle(window.screen)
ball = Ball(window.screen)
blocks = Blocks(window.screen)
blockslist = blocks.create_blocks(window.screen)

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
        paddle.xposition -= 5
        paddle.move(window.screen)

    if key_input[pygame.K_RIGHT] and paddle.xposition<900:
        paddle.xposition += 5
        paddle.move(window.screen)
#Check collision
    ball.check_paddle_collision(window.screen,paddle.paddle,blockslist)

#Moving Ball
    ball.move_ball(window.screen)
#Allows us to set a refreh rate
    fpsclock.tick(fps)









