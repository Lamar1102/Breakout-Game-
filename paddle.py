import pygame

class Paddle:
    def __init__(self,window):
        ##start posiition
        self.xposition = 450
        self.paddle = pygame.draw.rect(window, "red", pygame.Rect(self.xposition, 700, 200, 30))
        pygame.display.update()


    def move(self,window):
        ### Colors old rectangle black to redraw moved paddle
        window.fill("black",self.paddle)
        self.paddle = pygame.draw.rect(window, "red", pygame.Rect(self.xposition, 700, 200, 30))

