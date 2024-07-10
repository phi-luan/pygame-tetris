from .block import Block
from .unit import Unit

import constants as const
class T_Block(Block):
    def __init__(self):
        super().__init__(const.PURPLE)
        first = Unit([3, 0], const.PURPLE)
        second = Unit([4, 0], const.PURPLE)
        third = Unit([5, 0], const.PURPLE)
        fourth = Unit([4, 1], const.PURPLE)
        
        self.units.add(first, second, third, fourth)

    def get_still_image(self):
        return [[(True, const.PURPLE) if (i == 0 and j != 3) or (i == 1 and j == 1) else (False, const.WHITE) for i in range(2) ] for j in range(4)]