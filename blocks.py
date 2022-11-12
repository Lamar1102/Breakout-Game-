import pygame

class Blocks:
    def __init__(self,window,x=-50,y=-50):
        self.hit = False

        self.block = pygame.draw.rect(window, "white", pygame.Rect(x, y, 75, 15))

    def create_blocks(self,window):
        blocks_list = []
        xposition = 5
        yposition = 50
        for i in range(15):

            block = Blocks(window,xposition,yposition)
            blocks_list.append(block)

            xposition+=80

        pygame.display.update()
        return blocks_list

    def fill_blocks(self,window):
        for block in self.blocks_list:

            window.fill("white",block)
            pygame.display.update()
