from .block import Block
from .unit import Unit

import constants as const
class J_Block(Block):
    def __init__(self):
        super().__init__(const.ORANGE)
        first = Unit([4, 0], const.ORANGE)
        second = Unit([4, 1], const.ORANGE)
        third = Unit([4, 2], const.ORANGE)
        fourth = Unit([3, 2], const.ORANGE)
        
        self.units.add(first, second, third, fourth)

    def get_still_image(self):
        return [[(True, const.ORANGE) if (i == 1 and j != 3) or (j == 2) else (False, const.WHITE) for i in range(2) ] for j in range(4)]