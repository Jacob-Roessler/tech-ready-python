import pygame
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen_width = 800
screen_height = 600
gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TEST')
clock = pygame.time.Clock()

class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.isjumping = False
        self.isfalling = True
        self.ismoving  = False
    def input(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x -= self.speed
            elif event.key == pygame.K_RIGHT:
                self.x += self.speed
            elif event.key == pygame.K_UP:
                self.y += self.speed
            elif event.key == pygame.K_DOWN:
                self.y += self.speed

    def move():
        if self.isfalling == True:
            self.y -= self.speed
        
    
font = pygame.font.SysFont(None, 30)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [screen_height/2, screen_width/2])

def gameloop():

    gameExit = False
    gameOver = False
    p1 = player(250, 250)
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            input(event)

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, blue, [p1.x,p1.y, 10, 20])
        for p in range(0,1000, 50):
            pygame.draw.rect(gameDisplay, black, [0+p, 400, 25, 25])
        pygame.display.update()
        clock.tick(30)


gameloop()