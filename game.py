
import pygame as pg
from sys import exit
from displayboard import S_BOARD
from enemy import Enemy
from game_stats import GameStats
from ship import Ship
from settings import Settings
from lasers import Laser
from pygame.sprite import Group
from game_functions import *

pg.init()

mainSettings = Settings()
screen = pg.display.set_mode((mainSettings.main_width, mainSettings.main_depth))
screen.fill(mainSettings.main_color)
pg.display.set_caption(mainSettings.gameName)

# Game Clock.
clock = pg.time.Clock()

# Creating a ship object
box= Ship(mainSettings, screen)

# Creating a enemy object.
enemy = Group()

# Creating a Laser Group
laser = Group()

# Create an object to store game statistics.
stats = GameStats(mainSettings)
hood = S_BOARD(mainSettings, screen, stats)

# Infinite gameloop
while True:
    check_events(mainSettings, box, laser, screen)
    if stats.game_state:
        updateLaser(mainSettings, screen, enemy, laser, stats, hood)
        update_enemies(mainSettings, screen, enemy, laser, box, stats, hood)
        update_screen(mainSettings, screen, box, laser, enemy, hood)
    else:
        if not stats.main_screen:
            main_screen(screen, mainSettings, hood, stats, clock)
        else:
            game_over(screen, box, stats, hood, laser, enemy, clock)
            pass
    clock.tick(60)
