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