import pygame
from unit import Unit

import constants as const

class Block:
    def __init__(self, color):
        self.units = pygame.sprite.Group()
        self.color = color

    def move(self, direction):
        if direction == 'left':
            for unit in self.units:
                if unit.rect.left <= const.GRID_START_X:
                    return
            for unit in self.units:
                unit.rect.x -= const.BLOCK_SIZE
                unit.x -= const.BLOCK_SIZE
        elif direction == 'right':
            for unit in self.units:
                if unit.rect.right >= const.GRID_END_X:
                    return
            for unit in self.units:
                unit.rect.x += const.BLOCK_SIZE
                unit.x += const.BLOCK_SIZE
        elif direction == 'down':
            for unit in self.units:
                unit.rect.y += const.BLOCK_SIZE
                unit.y += const.BLOCK_SIZE

    def check_collision(self, next_frame_event) -> bool:
        for unit in self.units:
            if unit.convert_to_coordinates()[1] == const.BOARD_HEIGHT:
                pygame.time.set_timer(next_frame_event, 0)
                return True
        return False

    def update_unit_coordinates(self, board, next_frame_event):
        if not self.check_collision(next_frame_event):
            for block in self.units:
                block.fall()
        else:
            board.add_block(self)
            pygame.time.set_timer(next_frame_event, 500)
            self.units = None
        

    def draw(self, surface):
        self.units.draw(surface)
