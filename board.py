import constants as const

class Board:
    def __init__(self) -> None:
        self.coordinates = [[(False, const.WHITE) for i in range(const.BOARD_WIDTH)] for j in range(const.BOARD_HEIGHT)]

    def add_block(self, block):
        
        for unit in block.units:
            i = unit.convert_to_coordinates()[0]
            j = unit.convert_to_coordinates()[1] - 1
            self.coordinates[j][i] = (True, block.color)
        
        for row in self.coordinates:
            print(row)
