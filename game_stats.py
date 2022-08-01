class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, mainsettings):
        """Initialize statistics."""
        self.settings = mainsettings
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_state = False
        self.main_screen = False
        self.score = 0
        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_lives