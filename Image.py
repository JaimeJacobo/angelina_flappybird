import pygame, random

class Image:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.x = x
        self.y = y
        self. width = width
        self.height = height
        self.resized_image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.resized_image, (self.x, self.y))

    def move_left(self):
        self.x = self.x - 2

    def reset_x(self):
        self.x = 340

    def reset_y(self):
        self.y = random.randint(250, 380)

    def reset_upper_pipe_y(self, lower_pipe_y, s):
        self.y = lower_pipe_y - self.height - s
