import pygame
import pygame.font
from pygame.sprite import Group

from ship import Ship

class S_BOARD():
    """Displays Scoring Information."""
    def __init__(self, mainSettings, screen, stats):
        """Initialize Scorekeeping."""
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.settings = mainSettings
        self.stats = stats

        # Font settings for scoring information.
        self.txt_color = (255, 118, 0)
        self.dis_font = pygame.font.Font("Font/SuperLegendBoy.ttf", 27)
        # self.dis_font = pygame.font.SysFont(None, 9)

        # Prepare the initial score
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()
        
    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "SCORE: {:,}".format(rounded_score)
        self.score_image = self.dis_font.render(score_str, True, self.txt_color, self.settings.main_color)
        # print(self.stats.score)

        # Display the score at the top left of the screen. 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.score_rect.bottom + 10
        
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "HIGH-SCORE: {:,}".format(high_score)
        self.high_score_image = self.dis_font.render(high_score_str, True, self.txt_color, self.settings.main_color)

        # > Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        # print(self.high_score_rect)
        
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships_lefts = self.stats.ships_left
        self.ship_display = self.dis_font.render("Ships Left: {}".format(self.ships_lefts), True, self.txt_color, self.settings.main_color)
        
        self.ship_display_rect = self.ship_display.get_rect()
        self.ship_display_rect.x = len("#######") + 4
        self.ship_display_rect.top = self.score_rect.top
        
    def displayhood(self):
        """Draw the stats on the screen."""
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()
        
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.ship_display, self.ship_display_rect)

        