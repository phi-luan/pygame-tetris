import pygame
import numpy as np
from random import randint
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

def draw_game_interface(board, next_block, block_held):

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
    
    write_text()
    draw_next_interface(next_block)
    draw_hold_interface(block_held)
    
def draw_next_interface(next_block):
    next_start_x = const.GRID_END_X + 30
    next_end_x = const.GRID_END_X + 90
    next_start_y = const.GRID_START_Y
    next_end_y = const.GRID_START_Y + 120
    
    still_image = next_block.get_still_image()
    for x in range(next_start_x, next_end_x, const.BLOCK_SIZE):
        for y in range(next_start_y, next_end_y, const.BLOCK_SIZE):
            i, j = ((x - next_start_x) // const.BLOCK_SIZE, (y - next_start_y) // const.BLOCK_SIZE)
            filled, color = still_image[j][i]
            
            if filled:
                pygame.draw.rect(SCREEN, color, (x, y, const.BLOCK_SIZE, const.BLOCK_SIZE))
            else:
                rect = pygame.Rect(x, y, const.BLOCK_SIZE, const.BLOCK_SIZE)
                pygame.draw.rect(SCREEN, const.WHITE, rect, 1) 

def draw_hold_interface(block_held):
    hold_start_x = const.GRID_START_X - 90
    hold_end_x = const.GRID_START_X - 30
    hold_start_y = const.GRID_START_Y
    hold_end_y = const.GRID_START_Y + 120

    try:
        still_image = block_held.get_still_image()
    except Exception as e:
        still_image = None

    for x in range(hold_start_x, hold_end_x, const.BLOCK_SIZE):
        for y in range(hold_start_y, hold_end_y, const.BLOCK_SIZE):
            if still_image == None:
                rect = pygame.Rect(x, y, const.BLOCK_SIZE, const.BLOCK_SIZE)
                pygame.draw.rect(SCREEN, const.WHITE, rect, 1) 
            else:
                i, j = ((x - hold_start_x) // const.BLOCK_SIZE, (y - hold_start_y) // const.BLOCK_SIZE)
                filled, color = still_image[j][i]
            
                if filled:
                    pygame.draw.rect(SCREEN, color, (x, y, const.BLOCK_SIZE, const.BLOCK_SIZE))
                else:
                    rect = pygame.Rect(x, y, const.BLOCK_SIZE, const.BLOCK_SIZE)
                    pygame.draw.rect(SCREEN, const.WHITE, rect, 1) 
                       
def write_text():
    text_font = pygame.font.Font("font/Pixeltype.ttf", 43)
    next_message = text_font.render(f'NEXT', False, const.WHITE)
    next_message_rect = next_message.get_rect(bottomleft=(const.GRID_END_X + 30, const.GRID_START_Y))
    hold_message = text_font.render(f'HOLD', False, const.WHITE)
    hold_message_rect = next_message.get_rect(bottomleft=(const.GRID_START_X - 90, const.GRID_START_Y))
    SCREEN.blit(next_message, next_message_rect)
    SCREEN.blit(hold_message, hold_message_rect)

def hold(current_block, block_held):
    if block_held == None:
        block_held = type(current_block)()
        current_block.is_settled = True
    else:
        current_block, block_held = type(block_held)(), type(current_block)()
        
    return current_block, block_held

def check_user_input(current_block, block_held, hold_allowed, board, turn_right_sound):
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
                turn_right_sound.play()
            elif event.key == pygame.K_e and hold_allowed:
                current_block, block_held = hold(current_block, block_held)
                hold_allowed = False
        
    return current_block, block_held, hold_allowed

        
def draw_menu_interface(blink, show_press_message):
    SCREEN.fill(const.BLACK)
    
    title_font = pygame.font.Font("font/Pixeltype.ttf", 250)
    press_font = pygame.font.Font("font/Pixeltype.ttf", 50)
    
    title_message = title_font.render(f'TETRIS', False, const.WHITE)
    title_message_rect = title_message.get_rect(center=(const.WINDOW_WIDTH/2, const.WINDOW_HEIGHT/2.5))
    
    press_message = press_font.render(f'PRESS ENTER TO PLAY', False, const.WHITE)
    press_message_rect = press_message.get_rect(center=(const.WINDOW_WIDTH/2, const.WINDOW_HEIGHT/1.5))

    SCREEN.blit(title_message, title_message_rect)
    
    if show_press_message:
        SCREEN.blit(press_message, press_message_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return True, Board(), show_press_message
        elif event.type == blink:
            show_press_message = not show_press_message

    return False, None, show_press_message

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()

    pygame.display.set_caption('Tetris')
    
    board = Board()
    blocks = [I_Block, L_Block, J_Block, O_Block, T_Block, S_Block, Z_Block]
    current_block = choice(blocks)()
    next_block = choice(blocks)()
    block_held = None
    hold_allowed = True
    game_active = False
    
    blink = pygame.USEREVENT + 2
    pygame.time.set_timer(blink, 700)
    show_press_message = True
    
    bg_music = pygame.mixer.Sound('audio/Tetris.mp3')
    bg_music.set_volume(0.1)
    turn_right_sound = pygame.mixer.Sound('audio/turn-block.mp3')
    turn_right_sound.set_volume(0.5)
    you_lose_sound = pygame.mixer.Sound('audio/you-lose-sound.wav')
    you_lose_sound.set_volume(1)
   

    bg_music.play(loops=-1)
    while True:
        while game_active:
            current_block, block_held, hold_allowed = check_user_input(current_block, block_held, hold_allowed, board, turn_right_sound)
            draw_game_interface(board, next_block, block_held)

            if current_block.is_settled:
                if board.is_end_game():
                    you_lose_sound.play()
                    game_active = False

                current_block = next_block
                next_block = choice(blocks)()
                hold_allowed = True
                pygame.time.set_timer(current_block.next_frame_event, 400)

            current_block.draw(SCREEN)
            pygame.display.update()
            CLOCK.tick(60)
        
        game_active, board, show_press_message = draw_menu_interface(blink, show_press_message)
        

if __name__ == "__main__":
    main()