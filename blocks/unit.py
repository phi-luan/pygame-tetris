import pygame
import constants as const

class Unit(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface([const.BLOCK_SIZE, const.BLOCK_SIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.rect.bottomleft = (x, y)

    def fall(self):
        self.rect.y += const.BLOCK_SIZE
        self.y += const.BLOCK_SIZE

    def convert_to_coordinates(self) -> tuple:
        return ((self.x - const.GRID_START_X) // const.BLOCK_SIZE, (self.y - const.GRID_START_Y) // const.BLOCK_SIZE)

    def __str__(self) -> str:
        return f'{self.convert_to_coordinates()}'
