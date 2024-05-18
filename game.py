
# Imports
import pygame, random
from Image import Image
clock = pygame.time.Clock()

# Pygame init
pygame.init()

# Pipe 1
pipe_x = 340  
pipe_y = random.randint(250, 380)
pipe_width = 52
pipe_height = 320

# Pipe 2
pipe2_x = pipe_x + 200
pipe2_y = random.randint(250, 380)
pipe2_width = 52
pipe2_height = 320

# Up Pipe 1
up_pipe_x = 340
up_pipe_y = pipe_y - 30
up_pipe_width = 52
up_pipe_height = 320

# Up Pipe 2
up_pipe2_x = 340
up_pipe2_y = pipe2_y - 30
up_pipe2_width = 52
up_pipe2_height = 320

# Base
base_y = 450
base_x = 0
base_width = 336
base_height = 112


# Screen
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))

# Create images
background_image = Image('sprites/background-day.png', 0, 0, 288, 512)
green_pipe = Image('sprites/pipe-green.png', pipe_x, pipe_y, pipe_width, pipe_height)
green_pipe2 = Image('sprites/pipe-green.png', pipe2_x, pipe2_y, pipe2_width, pipe2_height)
up_pipe1 = Image('sprites/pipe-green-up.png', up_pipe_x, up_pipe_y, pipe2_width, pipe2_height)
up_pipe2 = Image('sprites/pipe-green-up.png', pipe2_x, pipe2_y, pipe2_width, pipe2_height)
base = Image('sprites/base.png', base_x, base_y, base_width, base_height)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw
    background_image.draw(screen)
    green_pipe.draw(screen)
    green_pipe2.draw(screen)
    up_pipe1.draw
    up_pipe2
    base.draw(screen)
    
    
    # Update
    green_pipe.move_left()
    green_pipe2.move_left()
    if green_pipe.x < -52:
        green_pipe.reset_x()
        green_pipe.reset_y()
    if green_pipe2.x < -52:
        green_pipe2.reset_x()
        green_pipe2.reset_y()

    pygame.display.flip()
    clock.tick(60)
pygame.quit()