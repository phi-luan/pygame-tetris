from .block import Block
from .unit import Unit

import constants as const
class I_Block(Block):
    def __init__(self):
        super().__init__(const.CYAN)
        first = Unit([4, 0], const.CYAN)
        second = Unit([4, 1], const.CYAN)
        third = Unit([4, 2], const.CYAN)
        fourth = Unit([4, 3], const.CYAN)
        
        self.units.add(first, second, third, fourth)
