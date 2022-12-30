import pygame


class Car:

    def __init__(self, game):
        # initiated self.screen just because all the elemnents of this module can use it later\

        # get the screen and it's rectangle
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # load the image and it's rectangle
        self.image = pygame.image.load('extra resources\car\car-3.bmp')
        self.image_rect = self.image.get_rect()

        self.image_rect.midright = self.screen_rect.midright

        # Car import settings
        self.settings = game.settings

        # Car Speed
        self.settings.car_speed = float(game.settings.car_speed)

        # Car moving buttons
        self.car_up = False
        self.car_right = False
        self.car_down = False
        self.car_left = False
        self.car_speed_increase = False
        self.car_speed_decrease = False

        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)

    def update(self):
        if self.car_up and self.image_rect.top > 0:
            self.y -= self.settings.car_speed
        elif self.car_right and self.image_rect.right < self.screen_rect.right:
            self.x += self.settings.car_speed
        elif self.car_left and self.image_rect.left > 0:
            self.x -= self.settings.car_speed
        elif self.car_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.car_speed
        elif self.car_speed_increase:
            self.settings.car_speed += 0.001
        elif self.car_speed_decrease and self.settings.car_speed > 0.002:
            self.settings.car_speed -= 0.001

        # Update back the x and y co-ordinates of the car
        self.image_rect.x = self.x
        self.image_rect.y = self.y

    def blitime(self):
        self.screen.blit(self.image, self.image_rect)
