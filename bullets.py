import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    def __init__(self, ai_game):
        # Get the settings for screen rectangle
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image_rect = ai_game.car.image_rect

        self.image = pygame.image.load('extra resources/bullet1.png')
        self.rect = self.image.get_rect()

        # Set the image bullet(image rect to the mid left of car image
        self.rect.midleft = self.image_rect.midleft

        self.x = float(self.rect.x)

        self.bullet_fire = False

    def update(self):
        self.rect.x -= 1

    def drawBullet(self):
        self.screen.blit(self.image, self.rect)
