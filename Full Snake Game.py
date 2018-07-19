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

#Screen, Clock, and Caption Definition
screen_width = 800
screen_height = 600
gameDisplay = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()


#Give Player class all attributes
class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity_x = 0
        self.velocity_y = 0
        self.snakeList = []
        self.snakeHead = []
        self.snakeHead.append(self.x)
        self.snakeHead.append(self.y)
        self.snakeList.append(self.snakeHead)
        self.lastPressed = "placeholder"
        self.length = 1

    def keys(self,event):
        #Gets User Input and disables moving in opposite direction
        #Movement is started by setting a speed then adding it later in the move method
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.lastPressed != "right":
                self.velocity_x = -block_speed
                self.velocity_y = 0
                self.lastPressed = "left"
            elif event.key == pygame.K_RIGHT and self.lastPressed != "left":
                self.velocity_x = block_speed
                self.velocity_y = 0
                self.lastPressed = "right"

            elif event.key == pygame.K_UP and self.lastPressed != "down":
                self.velocity_y = -block_speed
                self.velocity_x = 0
                self.lastPressed = "up"

            elif event.key == pygame.K_DOWN and self.lastPressed != "up":
                self.velocity_y = block_speed
                self.velocity_x = 0
                self.lastPressed = "down"

    def move(self):
        #Adds velocities to create movement
        self.x += self.velocity_x
        self.y += self.velocity_y
    def snake(self, block_size, snakelist):
        for XY in snakelist:
            pygame.draw.rect(gameDisplay, black, [XY[0], XY[1], block_size, block_size])
            #pygame.draw.circle(gameDisplay, black, [int(XY[0]), int(XY[1])], int(block_size/2))
class apple:
    #Class for apple attributes
    def __init__(self):
        self.x = 0
        self.y = 0
    #Function to set a random apple position in a 10px grid
    def setapple(self):
        self.x = round(random.randrange(0, screen_width - block_size) / 10.0) * 10.0
        self.y = round(random.randrange(0, screen_height - block_size) / 10.0) * 10.0
    def draw(self):
        pygame.draw.rect(gameDisplay, red, [self.x, self.y, block_size, block_size])

#Main Game settings for speed and size
block_speed = 10
block_size = 10
fps = 30
#Define player 1 object
p1 = player(0,0)
#Get system font for use with message to screen function
font = pygame.font.SysFont(None, 30)

def message_to_screen(msg, color, xpos, ypos):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [xpos, ypos])

#Function for main menu of game
def mainmenu():
    startGame = False
    while not startGame:
        gameDisplay.fill(black)
        message_to_screen("Welcome to Snake Game!", white, 200, 100)
        message_to_screen("by Jacob Roessler", white, 200, 150)
        message_to_screen("Press [SPACEBAR] to start", green, 200, 400)
        message_to_screen("Press [Q] to quit", red, 200, 450)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    startGame = True
        pygame.display.update()


#Main gameloop function
def gameloop(gameExit):
    global fps
    gameOver = False

    p1 = player(0, 0)
    p1.x = screen_width / 2
    p1.y = screen_height / 2

    #initialize snakeList outside of while loop
    p1.snakeList = []
    #Create randapple object and set random position
    randapple = apple()
    randapple.setapple()

    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over", black, 200, 300)
            message_to_screen(">Press C to continue", green, 225, 350)
            message_to_screen(">Press Q to quit", red, 225, 400)

            message_to_screen(f"Score: {p1.length-1}", black, 200, 250)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                    break

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                        quit()
                    elif event.key == pygame.K_c:
                        gameloop(gameExit)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            p1.keys(event)

        if p1.x >= screen_width or p1.x <= 0 or p1.y >= screen_height or p1.y <= 0:
            gameDisplay.fill(red)
            pygame.display.update()
            pygame.time.delay(100)
            gameOver = True
        #Moves Player
        p1.move()


        gameDisplay.fill(white)
        randapple.draw()

        #Create snake parts for every frame
        p1.snakeHead = []
        p1.snakeHead.append(p1.x)
        p1.snakeHead.append(p1.y)
        p1.snakeList.append(p1.snakeHead)
        p1.snake(block_size, p1.snakeList)

        #Properly keeps snake the right length by removing the first part appended depending on length
        if len(p1.snakeList) > p1.length:
            del p1.snakeList[0]

        #Collision checks if snake head runs into its body
        for eachSegment in p1.snakeList[:-1]:
            if eachSegment == p1.snakeHead:
                gameOver = True
        message_to_screen(f"Score: {p1.length-1}", blue, 0 , 0)
        pygame.display.update()
        #Collision check for apple 
        if p1.x == randapple.x and p1.y == randapple.y:
            p1.length += 100
            randapple.setapple()
            message_to_screen("+1", blue, p1.x+15, p1.y+15)
            pygame.display.update()

        clock.tick(fps)
########################################################################################################################
gameExit = False

mainmenu()
gameloop(gameExit)
pygame.display.update()
time.sleep(1)
pygame.quit()
quit()
