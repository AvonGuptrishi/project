from random import randint
import pygame as pg
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, mainSettings, screen):

        super(Enemy, self).__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pg.image.load("Graphics/box-black.png").convert_alpha()
        self.rect = self.image.get_rect(topright = (self.screen_rect.right, self.screen_rect.centery))

        self.mainSettings = mainSettings

        self.move_enemy1_x = self.rect.x =  self.screen_rect.width
        self.rect.y = randint(0, self.screen_rect.height-4)
        
    def blit_enemy(self):
        # for i in range(len(self.enemy_rect)):
        self.screen.blit(self.image, self.rect)

    def move_enemy(self):
        """Move the alien to the right of the screen."""
        self.move_enemy1_x -= 1.25
        # self.move_enemy2_x -= 1.25
        self.rect.x = self.move_enemy1_x
        # self.enemy2_rect.x = self.move_enemy2_x
    
    def check_edge(self):
        """Returns true if the enemy has reaches the left side edge of the screen."""
        if self.rect.left < 0:
            return True
        return False 