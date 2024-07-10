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