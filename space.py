from enum import Enum
from random import randint

class SpaceType(Enum):
  START = 'START'
  GOAL = 'GOAL'
  NORMAL = 'NORMAL'

class Space:
  def __init__(self, x, y, z, space_type):
    self.space_type = space_type
    self.x = x
    self.y = y
    self.z = z

  def next_one(self, lower_limits, upper_limits):
    is_done = False
    while not is_done:
      current = [self.x, self.y, self.z]
      x = randint(0, 2)
      y = randint(0, 1)
      current[x] = current[x] - 1 if y == 0 else current[x] + 1





    return current




