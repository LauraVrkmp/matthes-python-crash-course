import sys
from random import randint

import pygame

from star import Star

class Stars:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.screen_width = 800
        self.screen_heigth = 600

        self.stars = pygame.sprite.Group()

        self._create_stars()

    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.stars.draw(self.screen)
            pygame.display.flip()
            
    
    def _create_stars(self):
        star = Star(self)
        star_width , star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.screen_heigth - 3 * star_height):
            while current_x < (self.screen_width - 2 * star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width
            
            current_x = star_width
            current_y += 2 * star_height


    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position + self._get_star_offset()
        new_star.rect.y = y_position + self._get_star_offset()
        self.stars.add(new_star)


    def _get_star_offset(self):
        offset_size = 10
        return randint(-1 * offset_size, offset_size)


if __name__ == '__main__':
    s = Stars()
    s.run_game()