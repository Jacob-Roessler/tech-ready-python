import pygame
import time
import random
pygame.init()

#Color definition RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen_width = 800
screen_height = 600
gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()



class player:
    def __init__(self, velocity_x, velocity_y, segments):
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.segments = segments
    def setlocation(self, x, y):
        self.x = x
        self.y = y
    def keys(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity_x = -block_speed
                self.velocity_y = 0
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = block_speed
                self.velocity_y = 0

            elif event.key == pygame.K_UP:
                self.velocity_y = -block_speed
                self.velocity_x = 0

            elif event.key == pygame.K_DOWN:
                self.velocity_y = block_speed
                self.velocity_x = 0
    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
class apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

block_speed = 10
block_size = 10
fps = 30
p1 = player(0,0)
p1.setlocation(screen_width/2,screen_height/2)

font = pygame.font.SysFont(None, 30)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [screen_height/2, screen_width/2])

def gameloop():
    gameExit = False
    gameOver = False

    p1 = player(0, 0, 3)
    p1.setlocation(screen_width / 2, screen_height / 2)

    randapple = apple(round(random.randrange(0,screen_width-block_size)/10.0)*10.0, round(random.randrange(0, screen_height-block_size)/10.0)*10.0)

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, C to continue or Q to quit", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            p1.keys(event)

            if p1.x >= screen_width or p1.x <= 0 or p1.y >= screen_height or p1.y <= 0:
                gameDisplay.fill(red)
                pygame.display.update()
                pygame.time.delay(100)
                gameOver = True

        p1.move()


        gameDisplay.fill(white)
        apple.draw = pygame.draw.rect(gameDisplay, red, [randapple.x,randapple.y,block_size,block_size])
        p1.head = pygame.draw.rect(gameDisplay, black, [p1.x, p1.y, block_size, block_size])
        pygame.display.update()

        if p1.x == randapple.x and p1.y == randapple.y \
        or p1.x == randapple.x+5 and p1.y == randapple.y\
        or p1.x == randapple.x-5 and p1.y == randapple.y\
        or p1.x == randapple.x and p1.y == randapple.y-5\
        or p1.x == randapple.x and p1.y == randapple.y+5\
        or p1.x == randapple.x-5 and p1.y == randapple.y-5\
        or p1.x == randapple.x+5 and p1.y == randapple.y+5\
        :
            print("APPLE")

        clock.tick(fps)
########################################################################################################################
gameloop()
message_to_screen("Game Over!", red)
pygame.display.update()
time.sleep(1)
pygame.quit()
quit()
