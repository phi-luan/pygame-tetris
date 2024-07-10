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