import pygame
import numpy as np
from sys import exit
from random import choice
from board import Board

from blocks.i_block import I_Block
from blocks.L_block import L_Block
from blocks.o_block import O_Block
from blocks.j_block import J_Block
from blocks.t_block import T_Block
from blocks.s_block import S_Block
from blocks.z_block import Z_Block

import constants as const

def draw_grid(board):

    SCREEN.fill(const.BLACK)

    for x in range(const.GRID_START_X, const.GRID_END_X, const.BLOCK_SIZE):
        for y in range(const.GRID_START_Y, const.GRID_END_Y, const.BLOCK_SIZE):
            i, j = ((x - const.GRID_START_X) // const.BLOCK_SIZE, (y - const.GRID_START_Y) // const.BLOCK_SIZE)
            filled, color = board.coordinates[j][i]
            
            if filled:
                pygame.draw.rect(SCREEN, color, (x, y, const.BLOCK_SIZE, const.BLOCK_SIZE))
            else:
                rect = pygame.Rect(x, y, const.BLOCK_SIZE, const.BLOCK_SIZE)
                pygame.draw.rect(SCREEN, const.WHITE, rect, 1)   

def check_user_input(current_block, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == current_block.next_frame_event:
            current_block.update_frame(board)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_block.move_left(board)
            elif event.key == pygame.K_RIGHT:
                current_block.move_right(board)
            elif event.key == pygame.K_DOWN:
                current_block.move_down(board)
            elif event.key == pygame.K_UP:
                current_block.rotate_right(board)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    pygame.display.set_caption('Tetris')
    
    board = Board()
    blocks = [I_Block, L_Block, J_Block, O_Block, T_Block, S_Block, Z_Block]
    current_block = choice(blocks)()
   
    while True:
        check_user_input(current_block, board)
        draw_grid(board)

        if current_block.is_settled:
            current_block = choice(blocks)()
            pygame.time.set_timer(current_block.next_frame_event, 400)

        current_block.draw(SCREEN)
        pygame.display.update()
        CLOCK.tick(60)


if __name__ == "__main__":
    main()
