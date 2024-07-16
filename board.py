import constants as const
import pygame

class Board:
    def __init__(self) -> None:
        self.coordinates = [[(False, const.WHITE) for i in range(const.BOARD_WIDTH)] for j in range(const.BOARD_HEIGHT)]
        self.line_counter = 0
        self.line_clear_sound = pygame.mixer.Sound('audio/clear.wav')
        self.line_clear_sound.set_volume(0.7)

    def add_block(self, block):
        for unit in block.units:
            self.coordinates[unit.index_j][unit.index_i] = (True, block.color)

        self.clear_line()
    
    def clear_line(self):
            full_lines = [j for j in range(const.BOARD_HEIGHT) if all(self.coordinates[j][i][0] for i in range(const.BOARD_WIDTH))]
            if full_lines:
                for j in full_lines:
                    for k in range(j, 0, -1):
                        self.coordinates[k] = self.coordinates[k - 1][:]
                    self.coordinates[0] = [(False, const.WHITE) for _ in range(const.BOARD_WIDTH)]
            
                if len(full_lines) == 1:
                     self.line_counter += 100
                elif len(full_lines) == 2:
                     self.line_counter += 300
                elif len(full_lines) == 3:
                     self.line_counter += 500
                else:
                     self.line_counter += 800
                
                self.line_clear_sound.play()
    
    def is_end_game(self):
         return any(self.coordinates[0][i][0] for i in range(const.BOARD_WIDTH))    
         