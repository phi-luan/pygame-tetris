from .block import Block
from .unit import Unit

import constants as const
class I_Block(Block):
    def __init__(self):
        super().__init__(const.CYAN)
        first = Unit([6, 0], const.CYAN)
        second = Unit([5, 0], const.CYAN)
        third = Unit([4, 0], const.CYAN)
        fourth = Unit([3, 0], const.CYAN)
        
        self.units.add(first, second, third, fourth)

    def get_still_image(self):
        return [[(True, const.CYAN) if i == 0 else (False, const.WHITE) for i in range(2) ] for j in range(4)]