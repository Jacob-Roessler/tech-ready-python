# import pygame module
import pygame

# Start pygame
pygame.init()

# Create a display. (400, 300) is the size of the display and should be a tuple
screen = pygame.display.set_mode((400, 300))

# tracks whether the game is currently running
active = True

# This loop will run as long as active is True
while active:
    # Loop through the event queue. If we reach a QUIT event, set active to False
    # Once active is no longer True, the loop will no longer run
    for event in pygame.event.get():
        # Add a line of code here to print the event
        
        print(event)
        if event.type == pygame.QUIT:
            active = False

    # update the display
    pygame.display.flip()