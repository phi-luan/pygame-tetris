from .block import Block
from .unit import Unit

import constants as const
class Z_Block(Block):
    def __init__(self):
        super().__init__(const.RED)
        first = Unit([4, 0], const.RED)
        second = Unit([4, 1], const.RED)
        third = Unit([3, 0], const.RED)
        fourth = Unit([5, 1], const.RED)
        
        self.units.add(first, second, third, fourth)

    def get_still_image(self):
        return [[(True, const.RED) if (i == 0 and 0 < j <= 2) or (i == 1 and j < 2) else (False, const.WHITE) for i in range(2) ] for j in range(4)]