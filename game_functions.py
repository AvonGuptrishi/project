from random import randint
import pygame as pg
from enemy import Enemy 
from lasers import Laser
from pygame.sprite import Group

def check_events(mainSettings, box, laser, screen):
    """Responds to user inputs"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        # Take care of the movement of the ships.
        if event.type == pg.KEYDOWN:
            # Check the keydown funtion.
            key_presses(event, box, laser, mainSettings, screen)
            pass
        if event.type == pg.KEYUP:
            # Check the keyup function.
            key_releases(event, box)
            pass

def key_presses(event, box, laser, mainSettings, screen):
    if event.key == pg.K_UP or event.key == pg.K_w:
        box.move_up = True

    if event.key == pg.K_DOWN or event.key == pg.K_s:
        box.move_down = True

    if event.key == pg.K_LEFT or event.key == pg.K_a:
        box.move_left = True

    if event.key == pg.K_RIGHT or event.key == pg.K_d:
        box.move_right = True

    if event.key == pg.K_SPACE:
        addLasers(box ,laser, mainSettings, screen)
    pass

def key_releases(event, box): 

    if event.key == pg.K_ESCAPE:
        pg.quit()
        exit()

    if event.key == pg.K_UP:
        box.move_up = False

    if event.key == pg.K_DOWN:
        box.move_down = False

    if event.key == pg.K_LEFT:
        box.move_left = False

    if event.key == pg.K_RIGHT:
        box.move_right = False 

def addLasers(box ,laser, mainSettings, screen):
    new_Laser = Laser( mainSettings, screen, box)
    laser.add(new_Laser)

def updateLaser(mainSettings, screen, enemy, laser, stats, hood):
    laser.update()
    check_laser_enemy_collisions(mainSettings, screen, enemy, laser, stats, hood)
    for plasma in laser.copy():
        if plasma.rect.top < 0:
            laser.remove(plasma)

def update_screen(mainSettings, screen, box, laser, enemy, hood):
    """This function takes care of the view. Updates screen."""
    screen.fill(mainSettings.main_color)
    # DISPLAY SCORE
    # Draw all the bullets.
    for laser in laser.sprites():
        laser.shoot_laser()
    # Moving the ship around.
    box.movement()
    # Blitting Ship.
    box.blit_ship()
    # Blitting enemies.
    # update_enemies(mainSettings, screen, enemy, laser, box)
    # Makes the enemy appear on screen.
    enemy.draw(screen)
    # hood.prep_score()
    # hood.prep_high_score()
    # hood.prep_ships()
    hood.displayhood()
    pg.display.update()

def update_enemies(mainSettings, screen, enemy, laser, box, stats, hood):
    """Update the positions of the aliens in the screen."""
    if len(enemy) <= mainSettings.max_enemies:
        new_enemy = Enemy(mainSettings, screen)
        enemy.add(new_enemy)
    # Look for any alien-ship collisions.
    if pg.sprite.spritecollideany(box, enemy):
        ship_collide(enemy, box, stats, hood)
        pass
    # Make enemies appear on screen.
    for enemies in enemy:
        enemies.blit_enemy()
        enemies.move_enemy()
    # Deletes the enemy that has left the screen. 
    remove_leftedge_enemy(enemy)

def remove_leftedge_enemy(enemy):
    for enemies in enemy.copy():
        if enemies.check_edge():
            enemy.remove(enemies)

def check_laser_enemy_collisions(mainSettings, screen, enemy, laser, stats, hood):

    collisons = pg.sprite.groupcollide(laser, enemy, True, True)
    # CHECK FOR COLLISIONS.
    if collisons != None:
        for enemies in collisons.values():
            # INCREASE SCORE
            stats.score += ( mainSettings.score_points * len(enemies))
        # CHECK HIGH SCORE
        if stats.score > stats.high_score:
            stats.high_score = stats.score  
        # print("Score: {}; High-Score: {}".format(stats.score, stats.high_score))  
    hood.displayhood()
    if len(enemy) == 0:
        # Destroy lasers, speed up game, create new enemy.
        laser.empty()

def ship_collide(enemy, box, stats, hood):
    # Reduce the ship lives left.
    if stats.ships_left > 0:
        
        # Decrement the ships.
        # Change ships lives left.
        stats.ships_left += -1
        # print(pg.sprite.spritecollideany(box, enemy))        
        # Remove the collided enemy.
        enemy.remove(pg.sprite.spritecollideany(box, enemy))
        # print("Test Check - Ship Hit.")

        # Update the ships left in the display hood.
        hood.prep_ships()        
        pass
    else:
        stats.game_state = False
    pass

def game_over(screen, box, stats, hood, laser, enemy, clock):
    

    # change screen background
    game_over_color = (31, 70, 144)
    screen.fill(game_over_color)
    # prep final score and greetings 
    final_score = int(round(stats.score, -1))
    final_highscore = int(round(stats.high_score, -1))
    congrats = "NO NEW HIGH-SCORE. TRY AGAIN!!"
    if (final_score >= final_highscore & final_score != 0):
        congrats = "YOU ACHIEVED A NEW HIGH-SCORE!!"
    congrats_img = hood.dis_font.render(congrats, True, hood.txt_color, game_over_color)
    congrats_img_rect = congrats_img.get_rect(center = (600, 175))
    
    final_score_str = "YOUR FINAL SCORE: {:,}".format(final_score)
    final_score_str_img = hood.dis_font.render(final_score_str, True, hood.txt_color, game_over_color)
    final_score_str_img_rect = final_score_str_img.get_rect(center = (600, 225))
    # Display final score & greetings
    screen.blit(final_score_str_img, final_score_str_img_rect)
    screen.blit(congrats_img, congrats_img_rect)

    # Resetting the game.
    # Press Spacebar to Restart
    reset_game = "PRESS SPACBAR TO RETRY"
    reset_game_img = hood.dis_font.render(reset_game, True, hood.txt_color, game_over_color)
    reset_game_img_rect = reset_game_img.get_rect(center = (600, 525))
    if randint(1,2)%2 == 0:
        screen.blit(reset_game_img, reset_game_img_rect)
        clock.tick(5)
    # Footer - CS50 FINAL PROJECT By AVON GUPTRISHI
    title = "CS50 Final_Project By AVON GUPTRISHI."
    title_img = hood.dis_font.render(title, True, "#ffffff", game_over_color)
    title_img_rect = title_img.get_rect(center = (600, 600))
    screen.blit(title_img, title_img_rect)
    key = pg.key.get_pressed()
    if key[pg.K_SPACE]:
        laser.empty()
        enemy.empty()
        stats.reset_stats()
        stats.score = 0
        stats.game_state = True
        box.reset_ship()
        
    # Update Frame of the screen
    pg.display.update()
    pass

def main_screen(screen, mainSettings, hood, stats, clock):
    # Change Screen Baackground.
    startScreen_bgColor = (232, 170, 66)
    screen.fill(startScreen_bgColor)

    # TITLE - CS50 FINAL PROJECT By AVON GUPTRISHI
    title = "CS50 Final_Project By AVON GUPTRISHI."
    title_img = hood.dis_font.render(title, True, "#5A8F7B", startScreen_bgColor)
    title_img = pg.transform.rotozoom(title_img,0,1.4)
    title_img_rect = title_img.get_rect(center = (600, 100))
    screen.blit(title_img, title_img_rect)

    # Display Game Title
    gamename_img = hood.dis_font.render(mainSettings.gameName, True, "#3EDBF0", startScreen_bgColor)
    gamename_img = pg.transform.rotozoom(gamename_img,0,1.5)
    gamename_img_rect = gamename_img.get_rect(center = (600, 175))
    screen.blit(gamename_img, gamename_img_rect)
    
    # Use Arrow KEYS to move the ships and Spacebar to shoot.
    arrow = "Use arrow keys or W, A, S, D to move the ship."
    arrow_img = hood.dis_font.render(arrow, True, "#00FFDD", startScreen_bgColor)
    arrow_img_rect = arrow_img.get_rect(center = (600, 450))
    screen.blit(arrow_img, arrow_img_rect)
    bar = "Use SpaceBar to shoot lasers."
    bar_img = hood.dis_font.render(bar, True, "#00FFDD", startScreen_bgColor)
    bar_img_rect = bar_img.get_rect(center = (600, 500))
    screen.blit(bar_img, bar_img_rect)
    bar_start = "PRESS SPACEBAR TO START THE GAME." 
    bar_start_img = hood.dis_font.render(bar_start, True, "#D61C4E", startScreen_bgColor)
    bar_start_img_rect = bar_start_img.get_rect(center = (600, 350))
    
    if randint(0, 1)%2 == 0:
        screen.blit(bar_start_img, bar_start_img_rect)
        clock.tick(5)


    key = pg.key.get_pressed()
    if key[pg.K_SPACE]:
        stats.game_state = True
        stats.main_screen = True
    
    # Update Frame of the screen
    pg.display.update()
    pass