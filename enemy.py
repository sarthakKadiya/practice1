import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    """ Class to make enemy's"""

    def __init__(self, ai_game):
        # Import scree settings and screen width and height
        # Initiate Sprite class
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect

        # Load image and get it's rectangle
        self.image = pygame.image.load('extra resources/fire-wheel1.png')
        self.rect = self.image.get_rect()

        # Set image position to bottom left corner
        self.rect.y = self.rect.height
        self.rect.x = self.rect.width

        # Just for reference to get the y co-ordinate
        self.y = self.rect.y

    def update(self):
        self.y += self.settings.enemy_speed * self.settings.enemy_dir
        self.rect.y = self.y

    def check_edge(self):
        if (self.rect.bottom >= self.screen_rect.bottom) or (self.rect.top <= self.screen_rect.top):
            return True
