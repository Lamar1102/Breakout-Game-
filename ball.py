import pygame

class Ball:
    def __init__(self,window):

        self.ball = pygame.image.load("ball.png")
        self.ball = pygame.transform.scale(self.ball,(20,20))
        # self.rect_boundry = self.ball.get_rect()
        self.rect_boundry = pygame.draw.rect(window, "black", pygame.Rect(0, 200, 20, 20))
        self.speed=[3,3]

        self.ball_is_moving = True

    def move_ball(self,window):
        self.rect_boundry = self.rect_boundry.move(self.speed)

        if self.rect_boundry.left < 0 or self.rect_boundry.right>1200:
            self.speed[0]= -self.speed[0]
        if self.rect_boundry.top < 0:
            self.speed[1]= -self.speed[1]

        window.blit(self.ball,self.rect_boundry)
        pygame.display.update()
        window.fill("black", self.rect_boundry)

    def check_paddle_collision(self,window,paddle,block_list):
        collision = pygame.Rect.colliderect(self.rect_boundry,paddle)
        if collision:
            self.speed[1] = -self.speed[1]
            window.fill("red",paddle)

        for block in block_list:
            collision2 = pygame.Rect.colliderect(self.rect_boundry,block.block)

            if collision2 and block.hit:
                self.speed[1] = -self.speed[1]
                window.fill("black", block.block)
                break
            if collision2:
                block.hit = True
                self.speed[1] = -self.speed[1]
                window.fill("red",block.block)
                print(block.hit)
                break








