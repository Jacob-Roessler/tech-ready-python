import pygame
from math import pi
 
pygame.init()
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
 
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snake")
 
done = False
clock = pygame.time.Clock()
 
while not done:
 
    clock.tick(60)
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done=True

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [75, 10, 50, 20], 2)
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    '''
    pygame.draw.line(screen, GREEN, [0, 0], [50,30], 5)
    pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)
    pygame.draw.aaline(screen, GREEN, [0, 50],[50, 80], True)
   
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2) 
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20]) 
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
    pygame.draw.arc(screen, BLACK,[210, 75, 150, 125], 0, pi/2, 2)
    pygame.draw.arc(screen, GREEN,[210, 75, 150, 125], pi/2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi,3*pi/2, 2)
    pygame.draw.arc(screen, RED,  [210, 75, 150, 125], 3*pi/2, 2*pi, 2)
    pygame.draw.circle(screen, BLUE, [60, 250], 40)
    pygame.display.flip()
    '''
    pygame.display.flip()
pygame.quit()