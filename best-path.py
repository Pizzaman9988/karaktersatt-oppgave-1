import pygame
from pygame.locals import *

#Colors
GREEN_COLOR = pygame.Color(0, 255, 0)
BLACK_COLOR = pygame.Color(0, 0, 0)
WHITE_COLOR = pygame.Color(255, 255, 255)

#Pygame Setup
play_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Path with lowest risk')
bg_image = pygame.image.load("grid.jpg") # Loads the simplified grid image.

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
                running = False
                break
    
    play_surface.fill(WHITE_COLOR) # Fill the screen with white.
    play_surface.blit(bg_image, (0, 0)) # Render the background image.


    start_x = 290
    start_y = 60
    one_tile = 70
    width = 20

    pygame.draw.rect(play_surface, GREEN_COLOR, Rect(start_x, start_y, one_tile, width)) 
    pygame.draw.rect(play_surface, GREEN_COLOR, Rect(start_x + one_tile, start_y, width, one_tile*3 + width))
    pygame.draw.rect(play_surface, GREEN_COLOR, Rect(start_x - 2*one_tile, start_y + one_tile*3 + width, one_tile*3 + width, width))
    pygame.draw.rect(play_surface, GREEN_COLOR, Rect(start_x - 2*one_tile - width, start_y + one_tile*3 + width, width, one_tile))
    pygame.draw.rect(play_surface, GREEN_COLOR, Rect(start_x - 3*one_tile - width, start_y + one_tile*4 + width, one_tile + width, width))
    pygame.draw.rect(play_surface, GREEN_COLOR, Rect(start_x - 3*one_tile - width, start_y + one_tile*4 + width, width, one_tile + width))

    pygame.display.flip()