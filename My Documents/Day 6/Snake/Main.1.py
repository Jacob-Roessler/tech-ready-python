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
    x = []
    y = []

    def __init__(self, velocity_x, velocity_y, segments):
        startpos = 250
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.segments = segments
        self.direction = "NA"
        for x in range(segments):
            self.x.append(-100)
            self.y.append(-100)
        self.x[0] = startpos
        self.x[1] = startpos-block_size*1
        self.x[2] = startpos-block_size*2
        self.y[0] = startpos
        self.y[1] = startpos
        self.y[2] = startpos

    def keys(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.velocity_x = -block_speed
                self.velocity_y = 0
                self.direction = "left"
            elif event.key == pygame.K_RIGHT:
                self.velocity_x = block_speed
                self.velocity_y = 0
                self.direction = "right"
            elif event.key == pygame.K_UP:
                self.velocity_y = -block_speed
                self.velocity_x = 0
                self.direction = "up"
            elif event.key == pygame.K_DOWN:
                self.velocity_y = block_speed
                self.velocity_x = 0
                self.direction = "down"
            return self.direction
    def move(self):
        for s in range(self.segments):
            self.x[s] += self.velocity_x
            self.y[s] += self.velocity_y
    def draw(self, direction):
        if direction == "left":
            for s in range(self.segments):
                self.x[s] = self.x[0]+block_size
                self.y[s] = self.y[0]
        if direction == "right":
            for s in range(self.segments):
                self.x[s] = self.x[0]-block_size
                self.y[s] = self.y[0]
        if direction == "up":
            for s in range(self.segments):
                self.x[s] = self.x[0]
                self.y[s] = self.y[0]+block_size
        if direction == "down":
            for s in range(self.segments):
                self.x[s] = self.x[0]
                self.y[s] = self.y[0]-block_size
        for s in range(self.segments):
            pygame.draw.rect(gameDisplay, black, [p1.x[s], p1.y[s], block_size, block_size])      
    



        
class apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

block_speed = 10
block_size = 10
fps = 30    
p1 = player(0, 0, 3)


font = pygame.font.SysFont(None, 30)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [screen_height/2, screen_width/2])

def gameloop():
    gameExit = False
    gameOver = False


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

            if p1.x[0] >= screen_width or p1.x[0] <= 0 or p1.y[0] >= screen_height or p1.y[0] <= 0:
                gameDisplay.fill(red)
                pygame.display.update()
                pygame.time.delay(100)
                gameOver = True


        
        p1.move()
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randapple.x,randapple.y,block_size,block_size])
        p1.draw(p1.keys(event))
        pygame.display.update()

        if p1.x[0] == randapple.x and p1.y[0] == randapple.y:
            p1.segments += 1
            p1.x.append(p1.x[0]-block_size*p1.segments)
            p1.y.append(p1.y[0])
            randapple.x = round(random.randrange(0, screen_width-block_size)/10.0)*10.0
            randapple.y = round(random.randrange(0, screen_height-block_size)/10.0)*10.0
            pygame.display.update()
            
            print("APPLE")
                    
        pygame.display.update()

        clock.tick(fps)
########################################################################################################################
gameloop()
message_to_screen("Game Over!", red)
pygame.display.update()
time.sleep(1)
pygame.quit()
quit()
