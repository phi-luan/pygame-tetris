import pygame
from sys import exit
from board import Board
from i_block import I_Block

import constants as const

def draw_grid(board):
    for x in range(const.GRID_START_X, const.GRID_END_X, const.BLOCK_SIZE):
        for y in range(const.GRID_START_Y, const.GRID_END_Y, const.BLOCK_SIZE):
            i, j = ((x - const.GRID_START_X) // const.BLOCK_SIZE, (y - const.GRID_START_Y) // const.BLOCK_SIZE)
            filled, color = board.coordinates[j][i]
            
            if filled:
                pygame.draw.rect(SCREEN, color, (x, y, const.BLOCK_SIZE, const.BLOCK_SIZE))
            else:
                rect = pygame.Rect(x, y, const.BLOCK_SIZE, const.BLOCK_SIZE)
                pygame.draw.rect(SCREEN, const.WHITE, rect, 1)

def update_main_interface(board):
    SCREEN.fill(const.BLACK)
    draw_grid(board)

def check_user_input(current_block, board, next_frame_event):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == next_frame_event:
            current_block.update_unit_coordinates(board, next_frame_event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_block.move('left')
            elif event.key == pygame.K_RIGHT:
                current_block.move('right')
            elif event.key == pygame.K_DOWN:
                current_block.move('down')

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    pygame.display.set_caption('Tetris')
    
    board = Board()
    current_block = I_Block()
   
    next_frame_event = pygame.USEREVENT + 1
    pygame.time.set_timer(next_frame_event, 500)

    while True:
        check_user_input(current_block, board, next_frame_event)
        update_main_interface(board)
        if current_block.units == None:
            current_block = I_Block()
        current_block.draw(SCREEN)
        pygame.display.update()
        CLOCK.tick(60)

if __name__ == "__main__":
    main()
