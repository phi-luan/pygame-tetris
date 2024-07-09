from .block import Block
from .unit import Unit

import constants as const
class I_Block(Block):
    def __init__(self):
        super().__init__(const.BLUE)
        self.first = Unit(4, 0, const.BLUE)
        self.second = Unit(4, 1, const.BLUE)
        self.third = Unit(4, 2, const.BLUE)
        self.forth = Unit(4, 3, const.BLUE)
        
        self.units.add(self.first, self.second, self.third, self.forth)
