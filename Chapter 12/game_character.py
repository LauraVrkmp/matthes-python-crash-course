import sys

import pygame

class GameCharacter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("game_character.bmp")
        self.image = pygame.transform.rotozoom(self.image, 0, 2)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)
    

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()
            self.blitme()


if __name__ == '__main__':
    bs = GameCharacter()
    bs.run_game()