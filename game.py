
# Imports
import pygame, random
from Image import Image
clock = pygame.time.Clock()

# Pygame init
pygame.init()

# General variables
s = 130

# Pipe 1
pipe1_height = 320
pipe1_width = 52
pipe1_x = 288
pipe1_y = random.randint(250, 380)

# Pipe 2
pipe2_height = 320
pipe2_width = 52
pipe2_x = pipe1_x + 288
pipe2_y = random.randint(250, 380)

# Pipe 3
pipe3_height = 320
pipe3_width = 52
pipe3_x = 288
pipe3_y = pipe1_y - pipe3_height - s

# Pipe 4
pipe4_height = 320
pipe4_width = 52
pipe4_x = pipe3_x + 288
pipe4_y = pipe2_y - pipe4_height - s

# Base
base_height = 112
base_width = 336
base_y = 450
base_x = 0


# Screen
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))

# Create images
background_image = Image('sprites/background-day.png', 0, 0, 288, 512)

pipe1 = Image('sprites/pipe-green.png', pipe1_x, pipe1_y, pipe1_width, pipe1_height)
pipe2 = Image('sprites/pipe-green.png', pipe2_x, pipe2_y, pipe2_width, pipe2_height)
pipe3 = Image('sprites/pipe-green-up.png', pipe3_x, pipe3_y, pipe3_width, pipe3_height)
pipe4 = Image('sprites/pipe-green-up.png', pipe4_x, pipe4_y, pipe4_width, pipe4_height)

base = Image('sprites/base.png', base_x, base_y, base_width, base_height)

# Functions

def reset_pipes_position():
    if pipe1.x < -52:
        pipe1.reset_x()
        pipe1.reset_y()
    if pipe2.x < -52:
        pipe2.reset_x()
        pipe2.reset_y()
    if pipe3.x < -52:
        pipe3.reset_x()
        pipe3.reset_upper_pipe_y(pipe1.y, s)
    if pipe4.x < -52:
        pipe4.reset_x()
        pipe4.reset_upper_pipe_y(pipe2.y, s)

def draw_pipes():
    pipe1.draw(screen)
    pipe2.draw(screen)
    pipe3.draw(screen)
    pipe4.draw(screen)

def draw_background():
    background_image.draw(screen)

def draw_base():
    base.draw(screen)


def move_pipes():
    pipe1.move_left()
    pipe2.move_left()
    pipe3.move_left()
    pipe4.move_left()
    

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw
    draw_background()
    draw_pipes()
    draw_base()

    # Update
    move_pipes()
    reset_pipes_position()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
