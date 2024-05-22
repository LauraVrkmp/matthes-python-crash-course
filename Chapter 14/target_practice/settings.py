class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.target_color = (0, 0, 0)
        self.target_speed = 1
        self.target_width = 10
        self.target_height = 250
        self.target_direction = 1

        self.points_per_hit = 1
        
        self.miss_limit = 3