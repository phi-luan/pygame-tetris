import pygame
import numpy as np
from .unit import Unit
from random import choice

import constants as const

class Block:
    def __init__(self, color):
        self.units = pygame.sprite.Group()
        self.color = color
        self.next_frame_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.next_frame_event, 400)
        self.is_settled = False

    def delete(self):
        for sprite in self.units:
            sprite.kill()
        pygame.time.set_timer(self.next_frame_event, 0)
        self.is_settled = True
        

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

    def rotate_right(self, board):
        old_positions = np.array([[unit.index_i, unit.index_j] for unit in self.units])
        pivot = old_positions[1]
        rotation_matrix = np.array([[0, 1], [-1, 0]])

        translated_points = old_positions - pivot
        rotated_points = np.dot(rotation_matrix, translated_points.T).T
        new_positions = rotated_points + pivot

        for unit, new_pos in zip(self.units, new_positions):
            unit.index_i, unit.index_j = new_pos

        if (not self.has_collided(board)):
            for unit in self.units:
                i, j = unit.convert_index_to_pixel()
                unit.rect.bottomleft = (i, j)
        else:
            for unit, old_pos in zip(self.units, old_positions):
                unit.index_i, unit.index_j = old_pos

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
            board.add_block(self)
            self.delete()

    def draw(self, surface):
        self.units.draw(surface)
