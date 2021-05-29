import pygame
from pygame.locals import *

def draw_block():
    surface.fill((61, 148, 51))  # RGB values for background color (this method is needed to clear all the previous blocks in screen)
    surface.blit(block, (block_x, block_y))  # drawing block on surface
    pygame.display.flip()  # updating pygame screen

if __name__ == "__main__":
    pygame.init()    #initializes pygame

    surface =  pygame.display.set_mode((1000,500)) #display area for our game
    surface.fill((61,148,51)) #RGB values for background color

    block = pygame.image.load("resources/block.jpg").convert()  #loading block.jpg
    block_x = 100  #cordinates of the block
    block_y = 100

    surface.blit(block,(block_x,block_y))  #drawing block on surface

    pygame.display.flip() #updating pygame screen

    #event loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN: #keydown came from pygame locals
                if event.key == K_ESCAPE: #quit when ESC is pressed
                    running = False

                if event.key == K_UP:
                    block_y -= 10  #move up y cordinates
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10 #move down y cordinates
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False

