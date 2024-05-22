import sys

import pygame

class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))


    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(event.key)


if __name__ == '__main__':
    k = Keys()
    k.run_game()