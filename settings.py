class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Car speed
        self.car_speed = 2.0

        # Bullet speed
        self.bullet_speed = 2

        # Enemy speed and settings
        self.enemy_speed = 5.0
        # 1 for Up and -1 for Down
        self.enemy_dir = 1
        self.enemy_dropspeed = 10