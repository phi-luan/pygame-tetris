import pygame
import constants as const

class Unit(pygame.sprite.Sprite):
    def __init__(self, coordinates, color):
        super().__init__()
        self.image = pygame.Surface([const.BLOCK_SIZE, const.BLOCK_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.index_i = coordinates[0]
        self.index_j = coordinates[1]

        pixel_x, pixel_y = self.convert_index_to_pixel()
        self.rect.bottomleft = (pixel_x, pixel_y)

    def convert_index_to_pixel(self):
        pixel_x = const.GRID_START_X + self.index_i * const.BLOCK_SIZE
        pixel_y = const.GRID_START_Y + (1 + self.index_j) * const.BLOCK_SIZE

        return (pixel_x, pixel_y)
    
    def __str__(self) -> str:
        return f'{(self.index_i, self.index_j)}'
