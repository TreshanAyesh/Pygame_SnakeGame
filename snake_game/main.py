import pygame
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()  # loading block.jpg
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((61, 148,51))  # RGB values for background color (this method is needed to clear all the previous blocks in screen)
        self.parent_screen.blit(self.block, (self.x, self.y))  # drawing block on surface
        pygame.display.flip()  # updating pygame screen

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_down(self):
        self.y += 10
        self.draw()

class Game:
    def __init__(self):
        pygame.init()  # initializes pygame
        self.surface = pygame.display.set_mode((1000, 500))  # display area for our game
        self.surface.fill((61, 148, 51))  # RGB values for background color
        self.snake = Snake(self.surface)  #snake inside game class
        self.snake.draw() #draw the snake

    def run(self):
        # event loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:  # keydown came from pygame locals
                    if event.key == K_ESCAPE:  # quit when ESC is pressed
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False


if __name__ == "__main__":
    game = Game()
    game.run()



