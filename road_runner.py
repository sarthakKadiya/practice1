import sys
import pygame
from settings import Settings
from car import Car
from bullets import Bullets
from enemy import Enemy


class Roadrunner:

    def __init__(self):
        """Initialize the game and it's resources"""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Road Runner")

        self.car = Car(self)

        # Will work as a list for bullet objects
        self.bullet = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.car.update()
            self.bullet.update()
            self.enemy_update()

    def _check_events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            elif events.type == pygame.KEYDOWN:
                self._keydown_event(events)
            elif events.type == pygame.KEYUP:
                self._keyup_event(events)

    def _keydown_event(self, events):
        if events.key == pygame.K_UP:
            self.car.car_up = True
        elif events.key == pygame.K_DOWN:
            self.car.car_down = True
        elif events.key == pygame.K_RIGHT:
            self.car.car_right = True
        elif events.key == pygame.K_LEFT:
            self.car.car_left = True
        elif events.key == pygame.K_w:
            self.car.car_speed_increase = True
        elif events.key == pygame.K_s:
            self.car.car_speed_decrease = True
        elif events.key == pygame.K_SPACE:
            self._fire_bullet()
        elif events.key == pygame.K_x:
            sys.exit()

    def _keyup_event(self, events):
        if events.key == pygame.K_UP:
            self.car.car_up = False
        elif events.key == pygame.K_DOWN:
            self.car.car_down = False
        elif events.key == pygame.K_RIGHT:
            self.car.car_right = False
        elif events.key == pygame.K_LEFT:
            self.car.car_left = False
        elif events.key == pygame.K_w:
            self.car.car_speed_increase = False
        elif events.key == pygame.K_s:
            self.car.car_speed_decrease = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.car.blitime()
        # Draw bullets in the game with the help of drawBullet method in bullets class
        for bullets in self.bullet.sprites():
            bullets.drawBullet()
        self.enemy.draw(self.screen)

        pygame.display.flip()

    def _fire_bullet(self):
        new_bullets = Bullets(self)
        self.bullet.add(new_bullets)

    def _create_fleet(self):
        enemies = Enemy(self)
        enemy_width, enemy_height = enemies.rect.size
        # Get available space vertically to insert num of aliens
        available_space = self.screen.get_height() - (2 * enemy_height)
        available_space_horizontal = self.screen.get_width() - 2 * self.car.image_rect.width - (3 * enemy_width)
        num_of_row = available_space_horizontal // (2 * enemy_width)
        num_of_enemy = available_space // (2 * enemy_height)

        for row in range(num_of_row):
            for enemy in range(num_of_enemy):
                self._create_aliens(enemy, row)

    def _create_aliens(self, enemy, row):
        enemies = Enemy(self)
        enemy_width, enemy_height = enemies.rect.size
        enemies.rect.x = enemy_width + 2 * enemy_width * row
        enemies.rect.y = enemy_height + 2 * enemy_height * enemy
        self.enemy.add(enemies)

    def enemy_update(self):
        self._check_edge()
        self.enemy.update()

    def _check_edge(self):
        screen_rect = self.screen.get_rect()
        for enemy in self.enemy.sprites():
            if enemy.check_edge():
                self._change_direction()
                break

    def _change_direction(self, enemy):
        for enemy in self.enemy.sprites():
            enemy.rect.x += self.settings.enemy_dropspeed
        self.settings.enemy_dir = self.settings.enemy_dir * -1
ect.x += self.settings.enemy_dropspeed
 enemy.rect.x += self.settings.enemy_dropspeed


