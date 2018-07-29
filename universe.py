from collections import Counter
from space import Space, SpaceType
from drone import DroneFactory


def create_spaces_2(x, y, z):
  spaces = []
  for _x in range(x):
    y_spaces = []
    for _y in range(y):
      z_spaces = []
      for _z in range(z):
        space = Space(_x, _y, _z)
        z_spaces.append(space)
      y_spaces.append(z_spaces)
    spaces.append(y_spaces)
  return spaces

def set_start_and_goal(spaces, starting_cube, goal_cube):
  spaces[starting_cube['x']][starting_cube['y']][starting_cube['z']].space_type = SpaceType.START
  spaces[goal_cube['x']][goal_cube['y']][goal_cube['z']].space_type = SpaceType.GOAL

class Universe:
  def __init__(self, x, y, z, starting_cube, goal_cube, max_drone_per_box):
    self.x_size = x
    self.y_size = y
    self.z_size = z
    self.max_drone_per_box = max_drone_per_box
    self.spaces = create_spaces_2(x, y, z)
    set_start_and_goal(self.spaces, starting_cube, goal_cube)
    self.drone_factory = DroneFactory()
    self.starting_cube = self.spaces[starting_cube['x']][starting_cube['y']][starting_cube['z']]
    self.goal_cube = self.spaces[goal_cube['x']][goal_cube['y']][goal_cube['z']]

  def reset(self):
    self.drones = []
    self.cost = 0
    self.score = 0
    self.num_collision = 0

  def init_drones(self, num_drones):
    for _ in range(num_drones):
      drone = self.drone_factory.create_drone(self.starting_cube)
      self.drones.append(drone)

  def gen_solutions(self):
    for drone in self.drones:
      drone.fly_to_goal(self)

  ## TODO get all solutions and sort them and pick top two
    ## TODO generate 48
      ## with applying P_c and P_m

  def compute_cost_and_collision(self):
    max_route_length = 0
    for drone in self.drones:
      route_length = len(drone.flying_route)
      max_route_length = max(max_route_length, route_length)
      self.cost = self.cost + route_length

    for i in range(max_route_length):
      time_slice = [None] * len(self.drones)
      for x in range(len(self.drones)):
        drone = self.drones[x]
        time_slice[x] = drone.get_i_in_flying_route(i)
      counts = dict(Counter(time_slice))
      for k, v in counts.items():
        if k is not None and k.space_type == SpaceType.NORMAL and v > self.max_drone_per_box:
          self.num_collision += 1




