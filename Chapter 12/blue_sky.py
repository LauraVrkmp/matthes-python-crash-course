import sys

import pygame

class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (65, 105, 225)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == '__main__':
    bs = BlueSky()
    bs.run_game()