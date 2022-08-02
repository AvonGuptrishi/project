from random import randint
import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self,mainSettings, screen, box):
        """Create a bullet object at the ship's current position."""
        super(Laser, self).__init__() #Prepare our object to use as a Sprite.
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0,0, mainSettings.laser_width, mainSettings.laser_height)
        # Make the intial position of the laser the top of the ship.
        self.rect.right = box.rect.right
        self.rect.center = box.rect.center

        # Store the bullet's velocity as a decimal value.
        self.along_x = float(self.rect.x)
        index = randint(0, 3)
        self.color = mainSettings.laser_color[index]
        self.speed_factor = mainSettings.laser_speed

        # Shootig Signal Flag. -> True when Keydown ELSE False.
        self.shoot_bool = False
    
    def update(self):
        """Move the bullet along the x-axis screen."""
        # Update the decimal position of the bullet
        self.along_x += self.speed_factor
        # Update the rect postion 
        self.rect.x = self.along_x 
    
    def shoot_laser(self):
        """Draw the laser to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)