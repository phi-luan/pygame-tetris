from .block import Block
from .unit import Unit

import constants as const
class I_Block(Block):
    def __init__(self):
        super().__init__(const.BLUE)
        self.first = Unit(const.GRID_START_X + 4 * const.BLOCK_SIZE, const.GRID_END_Y - 19 * const.BLOCK_SIZE, const.BLUE)
        self.second = Unit(const.GRID_START_X + 4 * const.BLOCK_SIZE, const.GRID_END_Y - 18 * const.BLOCK_SIZE, const.BLUE)
        self.third = Unit(const.GRID_START_X + 4 * const.BLOCK_SIZE, const.GRID_END_Y - 17 * const.BLOCK_SIZE, const.BLUE)
        self.forth = Unit(const.GRID_START_X + 4 * const.BLOCK_SIZE, const.GRID_END_Y - 16 * const.BLOCK_SIZE, const.BLUE)
        
        self.units.add(self.first, self.second, self.third, self.forth)
