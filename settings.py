
class Settings():
    def __init__(self):
        # Screen Size.
        # Fix Background.
        self.main_width = 1200
        self.main_depth = 700
        self.main_color = (63, 78, 79)
        self.gameName = "ALIEN INVADERS"

        # Enter ship settings.
        # Ship Speed
        self.ship_speed = 3
        # Ship Lives.
        self.ship_lives = 10

        # Enemy settings.
        self.max_enemies = 50
        self.score_points = 10

        # Enter Laser Settings.
        self.laser_color = [(255, 0, 99), (255, 248, 10), (248, 6, 204), (169, 16, 121)]
        self.laser_width = 15
        self.laser_height = 4
        self.laser_speed = 1.5 * self.ship_speed
        pass