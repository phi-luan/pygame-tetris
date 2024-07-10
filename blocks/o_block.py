from .block import Block
from .unit import Unit

import constants as const
class O_Block(Block):
    def __init__(self):
        super().__init__(const.YELLOW)
        first = Unit([4, 0], const.YELLOW)
        second = Unit([4, 1], const.YELLOW)
        third = Unit([5, 0], const.YELLOW)
        fourth = Unit([5, 1], const.YELLOW)
        
        self.units.add(first, second, third, fourth)

    def rotate_right(self, board):
        pass
    