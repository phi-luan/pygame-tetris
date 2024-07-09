import pygame
from .unit import Unit

import constants as const

class Block:
    def __init__(self, color):
        self.units = pygame.sprite.Group()
        self.color = color
        self.next_frame_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.next_frame_event, 500)

    def move_left(self, board):
        # simulate move
        for unit in self.units:
            unit.index_i -= 1

        # if move possible, update frame
        if (not self.has_collided(board)):
            for unit in self.units:
                unit.rect.x -= const.BLOCK_SIZE
        else:
            for unit in self.units:
                unit.index_i += 1

    def move_right(self, board):
        # simulate move   
        for unit in self.units:
           unit.index_i += 1

        # if move possible, update frame
        if (not self.has_collided(board)):
            for unit in self.units:
                unit.rect.x += const.BLOCK_SIZE
        else:
            for unit in self.units:
                unit.index_i -= 1
    
    def move_down(self, board):
        # simulate move
        for unit in self.units:
            unit.index_j += 1

        # if move possible, update frame
        if (not self.has_collided(board)):
            for unit in self.units:
                unit.rect.y += const.BLOCK_SIZE
        else: 
            for unit in self.units:
                unit.index_j -= 1

    def fall(self):
        for unit in self.units:
            unit.index_j += 1
            unit.rect.y += const.BLOCK_SIZE

    def has_collided(self, board) -> bool:
        for unit in self.units:
            # check if the block has touched the ground
            if unit.index_j >= const.BOARD_HEIGHT - 1:
                return True
            # check if the block has touched the side borders
            elif unit.index_i < 0 or unit.index_i > 9:
                return True
            # check if the block has touched an another block
            elif board.coordinates[unit.index_j + 1][unit.index_i][0]:
                return True
        return False
   
    def update_frame(self, board):
        if not self.has_collided(board):
            self.fall()
        else:
            pygame.time.set_timer(self.next_frame_event, 0)
            board.add_block(self)
            self.units = None  # Careful: ensure this is the right approach to "deactivate" the current block

    def draw(self, surface):
        self.units.draw(surface)
