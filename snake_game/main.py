import pygame
from pygame.locals import *
import time  #timers for delays in snake.walk method

size = 40

class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = size * 10
        self.y = size * 10
    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))  # drawing block on surface
        pygame.display.flip()  # updating pygame screen


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()  # loading block.jpg
        self.x = [size] * length   #initializing list of length no.of elements
        self.y = [size] * length
        self.direction = "down"

    def draw(self):
        self.parent_screen.fill((61, 148,51))  # RGB values for background color (this method is needed to clear all the previous blocks in screen)
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))  # drawing block on surface
        pygame.display.flip()  # updating pygame screen

    def move_left(self):
        self.direction = 'left'  #now we have a walk method,it takes care of cordinates
        #self.x -= 10
        #self.draw()

    def move_right(self):
        self.direction = 'right'
        #self.x += 10
        #self.draw()

    def move_up(self):
        self.direction = 'up'
        #self.y -= 10
        #self.draw()

    def move_down(self):
        self.direction = 'down'
        #self.y += 10
        #self.draw()

    def walk(self):  #making the snake run on its own

        for i in range(self.length -1,0,-1):
            self.x[i] = self.x[i-1] #next x position is position of next block
            self.y[i] = self.y[i-1]

        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size

        self.draw()

class Game:
    def __init__(self):
        pygame.init()  # initializes pygame
        self.surface = pygame.display.set_mode((1000, 600))  # display area for our game
        self.surface.fill((61, 148, 51))  # RGB values for background color
        self.snake = Snake(self.surface,6)  #snake inside game class
        self.snake.draw() #draw the snake
        self.apple = Apple(self.surface) #initializing apple
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()  # needed because walk method clears the screen


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
            self.play()
            time.sleep(0.2)  #to make the snake move on its own

if __name__ == "__main__":
    game = Game()
    game.run()



