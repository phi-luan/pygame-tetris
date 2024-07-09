import pygame
import constants as const

class Unit(pygame.sprite.Sprite):
    def __init__(self, index_i, index_j, color):
        super().__init__()
        self.image = pygame.Surface([const.BLOCK_SIZE, const.BLOCK_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.index_i = index_i
        self.index_j = index_j

        pixel_x = const.GRID_START_X + self.index_i * const.BLOCK_SIZE
        pixel_y = const.GRID_START_Y + (1 + self.index_j) * const.BLOCK_SIZE
        self.rect.bottomleft = (pixel_x, pixel_y)

    def fall(self):
        self.rect.y += const.BLOCK_SIZE
        self.index_j += const.BLOCK_SIZE


    # def convert_to_coordinates(self) -> tuple:
    #     return ((self.x - const.GRID_START_X) // const.BLOCK_SIZE, (self.y - const.GRID_START_Y) // const.BLOCK_SIZE)

    def __str__(self) -> str:
        return f'{(self.index_i, self.index_j)}'
