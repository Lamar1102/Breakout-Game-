import pygame
import time

class Ball:
    def __init__(self,window):

        self.ball = pygame.image.load("ball.png")
        self.ball = pygame.transform.scale(self.ball,(15,15))
        # self.rect_boundry = self.ball.get_rect()
        self.rect_boundry = pygame.draw.rect(window, "black", pygame.Rect(0, 200, 20, 20))
        self.speed=[8,8]

        self.ball_is_moving = True

    def move_ball(self,window,paddle):
        self.rect_boundry = self.rect_boundry.move(self.speed)

        if self.rect_boundry.left < 0 or self.rect_boundry.right>1200:
            self.speed[0]= -self.speed[0]
        if self.rect_boundry.top < 0:
            self.speed[1]= -self.speed[1]

        window.blit(self.ball,self.rect_boundry)
        pygame.display.update()
        window.fill("black", self.rect_boundry)
        window.fill("red", paddle)

    def check_paddle_collision(self,window,paddle,block_list):
        paddle_xposition = self.rect_boundry.centerx
        ball_xposition = paddle.centerx
        difference = paddle_xposition - ball_xposition
        collision = pygame.Rect.colliderect(self.rect_boundry,paddle)
        ydifference = self.rect_boundry.bottom - paddle.top


        if collision and ydifference < 10:
            print(difference)

            if difference < 10 and difference >= -10:
                self.speed[0] = 0
                self.speed[1] = -16
                window.fill("red",paddle)
            elif difference > 10 and difference <= 20:
                self.speed[0] = 1
                self.speed[1] = -15
                window.fill("red", paddle)
            elif difference < -10 and difference >= -20:
                self.speed[0]=-1
                self.speed[1]=-15
                window.fill("red", paddle)
            elif difference > 20 and difference <= 30:
                self.speed[0] = 3
                self.speed[1] = -13
                window.fill("red", paddle)
            elif difference < -20 and difference >= -30:
                self.speed[0]=-3
                self.speed[1]=-13
                window.fill("red", paddle)
            elif difference > 30 and difference <= 40:
                self.speed[0] = 6
                self.speed[1] = -10
                window.fill("red", paddle)
            elif difference < -30 and difference >= -40:
                self.speed[0]=-6
                self.speed[1]=-10
                window.fill("red", paddle)
            elif difference > 40 and difference <= 50:
                self.speed[0] = 8
                self.speed[1] = -8
                window.fill("red", paddle)
            elif difference < -40 and difference >= -50:
                self.speed[0]=-8
                self.speed[1]=-8
                window.fill("red", paddle)
            elif difference > 50 and difference <= 60:
                self.speed[0] = 10
                self.speed[1] = -6
                window.fill("red", paddle)
            elif difference < -50 and difference >= -60:
                self.speed[0]=-10
                self.speed[1]=-6
                window.fill("red", paddle)
            elif difference < 60:
                self.speed[0] = -12
                self.speed[1] = -6
                window.fill("red", paddle)
            elif difference > 60:
                self.speed[0]=12
                self.speed[1]=-6
                window.fill("red", paddle)


        for block in block_list:
            collision2 = pygame.Rect.colliderect(self.rect_boundry,block.block)

            if collision2 and block.hit:
                self.speed[1] = -self.speed[1]
                block.move_block(window)
                break
            if collision2:
                block.hit = True
                self.speed[1] = -self.speed[1]
                window.fill("red",block.block)
                break

    def restart_ball(self,window):
        if self.rect_boundry.top > 800:

            self.speed = [5, 5]
            time.sleep(1)
            self.rect_boundry = pygame.draw.rect(window, "black", pygame.Rect(0, 200, 20, 20))

            return True

            time.sleep(1)
            self.rect_boundry = pygame.draw.rect(window, "black", pygame.Rect(0, 200, 20, 20))













