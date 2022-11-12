
import pygame
from paddle import Paddle

class Window:
    def __init__(self):
        #Initializing game window
        self.running = True

        pygame.init()

        self.screen_size = (1200,800)
        self.screen = pygame.display.set_mode(self.screen_size)




