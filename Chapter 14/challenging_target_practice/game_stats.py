class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.hitpoints = 0

    
    def reset_stats(self):
        self.num_hits = 0
        self.num_missed = 0