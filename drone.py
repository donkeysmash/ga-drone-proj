from space import SpaceType

class DroneFactory:
  def __init__(self):
    self.drone_id = 0

  def create_drone(self, starting):
    d_id = self.drone_id
    self.drone_id += 1
    return Drone(d_id, starting)

class Drone:
  def __init__(self, drone_id, init_block):
    self.drone_id = drone_id
    self.flying_route = [init_block]

  def fly_to_goal(self, spaces):
    last_block = self.flying_route[-1]
    if last_block.space_type == SpaceType.GOAL:
      return self.flying_route
    else:
      next_block_address = last_block.next_one()
      next_space = spaces[next_block_address[0]][next_block_address[1]][next_block_address[2]]
      self.flying_route.append(next_space)
      self.fly_to_goal(spaces)




    return self.flying_route