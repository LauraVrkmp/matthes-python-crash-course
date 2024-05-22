import sys

import pygame

from raindrop import Raindrop

class RainDrops:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_width = 1200
        self.screen_heigth = 800

        self.raindrops = pygame.sprite.Group()

        self._create_grid()


    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


    def _update_raindrops(self):
        self.raindrops.update()

        make_new_drops = False
        for drop in self.raindrops.copy():
            if drop.check_disappeared():
                self.raindrops.remove(drop)
                make_new_drops = True

        if make_new_drops:
            self._create_new_row()


    def _create_grid(self):
        raindrop = Raindrop(self)
        raindrop_width , raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_y < (self.screen_heigth - 3 * raindrop_height):
            while current_x < (self.screen_width - 2 * raindrop_width):
                self._create_raindrop(current_x, current_y)
                current_x += 2 * raindrop_width
            
            current_x = raindrop_width
            current_y += 2 * raindrop_height


    def _create_raindrop(self, x_position, y_position):
        new_raindrop = Raindrop(self)
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)  


    def _create_new_row(self):
        raindrop = Raindrop(self)
        raindrop_width , raindrop_height = raindrop.rect.size

        current_x, current_y = raindrop_width, raindrop_height
        while current_x < (self.screen_width - 2 * raindrop_width):
            self._create_raindrop(current_x, current_y)
            current_x += 2 * raindrop_width

    
    def _update_screen(self):
        self.screen.fill("black")
        self.raindrops.draw(self.screen)
        
        pygame.display.flip()


if __name__ == '__main__':
    rd = RainDrops()
    rd.run_game()