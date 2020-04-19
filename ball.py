import pygame
from random import randint

BLACK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.circle(self.image, color, (5, 5), 5)

        self.velocity = [randint(6, 7), randint(-15, 15)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.change_color((0, 255, 0))

        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-15, 15)

    def change_color(self, color):
        pygame.draw.circle(self.image, color, (5, 5), 5)
