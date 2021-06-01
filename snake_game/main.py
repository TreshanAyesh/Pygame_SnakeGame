import pygame
from pygame.locals import *
import time  #timers for delays in snake.walk method
import random  #to generate random numbers

size = 40
BACKGROUND_COLOR = (61, 148, 51)

class Apple:
    def __init__(self, parent_screen):
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = size * 10
        self.y = size * 10
    def draw(self):
        self.parent_screen.blit(self.apple, (self.x, self.y))  # drawing block on surface
        pygame.display.flip()  # updating pygame screen

    def move(self):
        self.x = random.randint(0,24) * size  #random x value less than 1000
        self.y = random.randint(0,14) * size


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()  # loading block.jpg
        self.x = [size] * length   #initializing list of length no.of elements
        self.y = [size] * length
        self.direction = "down"

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        #self.parent_screen.fill((61, 148,51))  # RGB values for background color (this method is needed to clear all the previous blocks in screen)
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
        pygame.display.set_caption("Snake Game by Treshan Ayesh")

        pygame.mixer.init()
        self.play_bg_music()

        self.surface = pygame.display.set_mode((1000, 600))  # display area for our game
        self.render_bg()  # RGB values for background color
        self.snake = Snake(self.surface,1)  #snake inside game class
        self.snake.draw() #draw the snake
        self.apple = Apple(self.surface) #initializing apple
        self.apple.draw()

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def reset(self):
        self.snake = Snake(self.surface, 1)  # snake inside game class
        self.apple = Apple(self.surface)  # initializing apple

    def play_bg_music(self):
        pygame.mixer.music.load("resources/bg_music_1.mp3")
        pygame.mixer.music.play()


    def play_sound(self, sound):
        sound = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sound)

    def render_bg(self):
        bg = pygame.image.load("resources/background.jpg").convert()
        self.surface.blit(bg, (0,0))

    def play(self):
        self.render_bg()
        self.snake.walk()
        self.apple.draw()  # needed because walk method clears the screen
        self.display_score()
        pygame.display.flip()

        #snake colliding with apple
        if self.is_collision(self.snake.x[0],self.snake.y[0], self.apple.x,self.apple.y):
           self.play_sound("ding")
           self.snake.increase_length()
           self.apple.move()
           print("Collision occurred")

        #snake colliding with itself
        for i in range(3, self.snake.length): #head can collide with 3rd block and ahead
            if self.is_collision(self.snake.x[0], self.snake.y[0],self.snake.x[i], self.snake.y[i]):
                self.play_sound("crash")
                raise "Game Over"


    def show_game_over(self):
        self.render_bg()
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game is Over! Your score is {self.snake.length}",True,(200,200,200))
        self.surface.blit(line1,(320,250))
        line2 = font.render("Press ENTER to play again. To exit press ESC",True,(200,200,200))
        self.surface.blit(line2,(250,290))
        pygame.display.flip()

        pygame.mixer.music.pause()


    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}",True,(200,200,200))
        self.surface.blit(score, (800,10))



    def run(self):
        # event loop
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:  # keydown came from pygame locals
                    if event.key == K_ESCAPE:  # quit when ESC is pressed
                        running = False

                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause = False

                    if not pause:
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

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.10)  #to make the snake move on its own

if __name__ == "__main__":
    game = Game()
    game.run()



