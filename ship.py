import pygame as pg

class Ship():

    def __init__(self, mainSettings, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.image = pg.image.load("Graphics/box-red.png").convert_alpha()
        self.rect = self.image.get_rect(midleft = (self.screen_rect.left, self.screen_rect.centery))
        
        self.mainSettings = mainSettings

        # Ship Movement.
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False

    def movement(self):
        """Make the ship move up, down, left, right."""
        along_y = 0
        if self.move_up:
            if self.rect.top >= self.screen_rect.top:
                along_y -= self.mainSettings.ship_speed
        if self.move_down:
            if self.rect.bottom <= self.screen_rect.bottom:
                along_y += self.mainSettings.ship_speed
        along_x = 0
        if self.move_left:
            if self.rect.left > 0:
                along_x -= self.mainSettings.ship_speed
        if self.move_right:
            if self.rect.right < self.screen_rect.right:
                along_x += self.mainSettings.ship_speed

        self.rect.centerx += along_x
        self.rect.centery += along_y

    def blit_ship(self):
        self.screen.blit(self.image, self.rect)

    def reset_ship(self):
        # Puts the ship in the starting positions.
        self.rect.midleft = (self.screen_rect.left, self.screen_rect.centery)
        self.screen.blit(self.image, self.rect)
