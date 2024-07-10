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