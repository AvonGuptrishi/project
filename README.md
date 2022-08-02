# PROJECT TITLE :- ALIEN INVADERS
#### Video Demo:  <URL HERE>
#### Description:
Tried to make an arcade game in python using the pygame library.
- The Game Loop basically consists of the player(A red box) shooting down the enemy(the incoming black boxes) until the ship left run out. 
- The program records whether you achieved a new High-Score or not.  
- The enemies randomly spawn from the right side of the screen and You have to shoot down the black boxes to score points.

- I also developed a Main Screen and a Game Over Screen
- The game over screen displays the high-score you achieved.
![GameOver Screen image](Pictures/gameover%20screen.png)

- The main screen prompts user to start the game by pressing spacebar and give instruction on how to move the ship.
![Main Screen image](Pictures/main%20screen.png)

- The Gameplay looks something like what is shown below.
![Game Screen image](Pictures/gameplay%20screen.png)

- Game Functions that run the game are:

![functions](Pictures/functions%20in%20game%20functions.png)

- Some of the game functions look like this:
    1. Game over screen:
    ```
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
    ```
    2. Main Screen Function.
    ```
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
    ```
    3. Ship maneuvering.
    ```
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
    ```
- Most of the game functions is handled by ```game_functions.py``` while the rest of the files contains classes and other support feature. Our main file is - ```game.py``` which contains our infinite gameloop and calls all the necessary functions from  ```game_functions.py```.
    1. Our gameloop looks like this:
    ```
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
    ```
    2. ```stats.game_state``` is a boolean variable that tells whether a game is active or not. 


