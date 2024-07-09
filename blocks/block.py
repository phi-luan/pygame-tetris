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

    def has_collided(self, board) -> bool:
        for unit in self.units:
            if unit.index_j == const.BOARD_HEIGHT or board.coordinates[unit.index_j][unit.index_i][0] == True :
                return True
            elif 0 >= unit.index_i >= 19:
                return True
        return False
   
    def update_frame(self, board):
        if (not self.has_collided(board)):
            self.move_down(board)
    
        else:
            pygame.time.set_timer(self.next_frame_event, 0)
            board.add_block(self)
            pygame.time.set_timer(self.next_frame_event, 500)
            self.units = None
        

    def draw(self, surface):
        self.units.draw(surface)
