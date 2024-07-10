from .block import Block
from .unit import Unit

import constants as const
class L_Block(Block):
    def __init__(self):
        super().__init__(const.BLUE)
        first = Unit([4, 0], const.BLUE)
        second = Unit([4, 1], const.BLUE)
        third = Unit([4, 2], const.BLUE)
        fourth = Unit([5, 2], const.BLUE)
        
        self.units.add(first, second, third, fourth)

    def get_still_image(self):
        return [[(True, const.BLUE) if (i == 0 and j != 3) or (j == 2) else (False, const.WHITE) for i in range(2) ] for j in range(4)]