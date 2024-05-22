class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.hitpoints = 0

    
    def reset_stats(self):
        self.hitpoints = 0
        self.num_missed = 0

    
    def increase_hitpoint(self):
        self.hitpoints += self.settings.points_per_hit