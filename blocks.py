import pygame

class Blocks:
    def __init__(self,window,x=-50,y=-50):
        self.hit = False
        self.level = 1

        self.block = pygame.draw.rect(window, "white", pygame.Rect(x, y, 75, 15))

    def create_blocks(self,window):
        blocks_list = []
        xposition = 500
        yposition = 50
        for i in range(1):

            block = Blocks(window,xposition,yposition)
            blocks_list.append(block)

            xposition+=80

        pygame.display.update()

        return blocks_list

    def create_blocks2(self,window):
        blocks_list = []
        xposition = 5
        yposition = 50
        for i in range(15):
            block = Blocks(window, xposition, yposition)
            blocks_list.append(block)

            xposition += 80
        xposition =5
        yposition += 60
        for i in range(15):


            block = Blocks(window, xposition, yposition)
            blocks_list.append(block)

            xposition += 80

            pygame.display.update()
        return blocks_list

    def move_block(self,window):
        window.fill("black",self.block)
        self.block = pygame.draw.rect(window, "white", pygame.Rect(-200, -200, 75, 15))
        pygame.display.update(self.block)

    def board_cleared(self,blocklist):
        cleared = False
        for block in blocklist:
            block_xposition = block.block.centerx
            if block_xposition < -10:
                cleared = True
            else:
                cleared = False
        return cleared

