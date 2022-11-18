import pygame

class Blocks:
    def __init__(self,window,x=-50,y=-50):
        self.hit = False
        self.level = 1

        self.block = pygame.draw.rect(window, "white", pygame.Rect(x, y, 75, 15))

    def display_lives(self,window,lives):
        life1= pygame.draw.rect(window, "white", pygame.Rect(20,760 , 5, 5))
        life2= pygame.draw.rect(window, "white", pygame.Rect(30,760 , 5, 5))
        life3= pygame.draw.rect(window, "white", pygame.Rect(40,760 , 5, 5))

        if lives ==2:
            window.fill("black",life3)
        elif lives==1:
            window.fill("black", life3)
            window.fill("black", life2)
        elif lives==0:
            window.fill("black")
            window.fill("black", life3)
            window.fill("black", life2)

    def display_level(self,window,level):
        font = pygame.font.SysFont(None, 15)
        level1 = font.render('Level 1', True, "gray")
        level1_boundry = pygame.draw.rect(window, "black", pygame.Rect(510, 400, 200, 20))

        level2 = font.render('Level 2', True, "gray")
        level2_boundry = pygame.draw.rect(window, "black", pygame.Rect(510, 400, 200, 20))

        level3 = font.render('Level 3', True, "gray")
        level3_boundry = pygame.draw.rect(window, "black", pygame.Rect(510, 400, 200, 20))

        level4 = font.render('Level 4', True, "gray")
        level4_boundry = pygame.draw.rect(window, "black", pygame.Rect(510, 400, 200, 20))

        if level == 1:
            window.blit(level1, level1_boundry)
        elif level == 2:
            window.blit(level2,level2_boundry)
        elif level ==3:
            window.blit(level3,level3_boundry)
        elif level ==4:
            window.blit(level4,level4_boundry)

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
        xposition = 420
        yposition = 50
        for i in range(3):

            block = Blocks(window,xposition,yposition)
            blocks_list.append(block)

            xposition+=80

        pygame.display.update()

        return blocks_list

    def create_blocks3(self,window):
        blocks_list = []
        xposition = 5
        yposition = 50
        for i in range(15):
            block = Blocks(window, xposition, yposition)
            blocks_list.append(block)

            xposition += 80

            pygame.display.update()
        return blocks_list



    def create_blocks4(self,window):
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
        list_length = len(blocklist)
        blocks_cleared = 0
        cleared = False
        for block in blocklist:
            block_xposition = block.block.centerx
            if block_xposition < -100:
                blocks_cleared += 1
            if blocks_cleared == list_length:
                cleared = True
        return cleared


