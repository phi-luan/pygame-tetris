from .block import Block
from .unit import Unit

import constants as const
class S_Block(Block):
    def __init__(self):
        super().__init__(const.GREEN)
        first = Unit([4, 0], const.GREEN)
        second = Unit([4, 1], const.GREEN)
        third = Unit([5, 0], const.GREEN)
        fourth = Unit([3, 1], const.GREEN)
        
        self.units.add(first, second, third, fourth)

    def get_still_image(self):
        return [[(True, const.GREEN) if (i == 0 and j < 2) or (i == 1 and 0 < j <= 2) else (False, const.WHITE) for i in range(2) ] for j in range(4)]