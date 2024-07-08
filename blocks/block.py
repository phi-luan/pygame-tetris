import pygame
from .unit import Unit

import constants as const

class Block:
    def __init__(self, color):
        self.units = pygame.sprite.Group()
        self.color = color

    def move(self, board, direction, next_frame_event):
        if direction == 'left':
            for unit in self.units:
                if unit.rect.left <= const.GRID_START_X or self.has_collided(board, next_frame_event):
                    return
            for unit in self.units:
                unit.rect.x -= const.BLOCK_SIZE
                unit.x -= const.BLOCK_SIZE
        elif direction == 'right' :
            for unit in self.units:
                if unit.rect.right >= const.GRID_END_X or self.has_collided(board, next_frame_event):
                    return
            for unit in self.units:
                unit.rect.x += const.BLOCK_SIZE
                unit.x += const.BLOCK_SIZE
        elif direction == 'down':
            for unit in self.units:
                unit.rect.y += const.BLOCK_SIZE
                unit.y += const.BLOCK_SIZE

    def has_collided(self, board, next_frame_event) -> bool:
        for unit in self.units:
            i,j = unit.convert_to_coordinates()
            if j == const.BOARD_HEIGHT:
                pygame.time.set_timer(next_frame_event, 0)
                return True
            elif board.coordinates[j][i][0]:
                pygame.time.set_timer(next_frame_event, 0)
                return True
        return False

    def update_unit_coordinates(self, board, next_frame_event):
        if not self.has_collided(board, next_frame_event):
            for block in self.units:
                block.fall()
        else:
            board.add_block(self)
            pygame.time.set_timer(next_frame_event, 500)
            self.units = None
        

    def draw(self, surface):
        self.units.draw(surface)
