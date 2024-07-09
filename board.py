import constants as const

class Board:
    def __init__(self) -> None:
        self.coordinates = [[(False, const.WHITE) for i in range(const.BOARD_WIDTH)] for j in range(const.BOARD_HEIGHT)]

    def add_block(self, block):
        for unit in block.units:
            self.coordinates[unit.index_j][unit.index_i] = (True, block.color)
        
