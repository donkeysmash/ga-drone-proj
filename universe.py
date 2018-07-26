from space import Space, SpaceType
from drone import DroneFactory

def check_coordinate(x, y, z, checker):
  return checker['x'] == x and checker['y'] == y and checker['z'] == z

def create_spaces(x, y, z, goal_cube, starting_cube):
  spaces = []
  for _x in range(x):
    y_spaces = []
    for _y in range(y):
      z_spaces = []
      for _z in range(z):
        if check_coordinate(_x, _y, _z, starting_cube):
          space_type = SpaceType.START
        elif check_coordinate(_x, _y, _z, goal_cube):
          space_type = SpaceType.GOAL
        else:
          space_type = SpaceType.NORMAL
        space = Space(_x, _y, _z, space_type)
        z_spaces.append(space)
      y_spaces.append(z_spaces)
    spaces.append(y_spaces)
  return spaces

class Universe:
  def __init__(self, x, y, z, starting_cube, goal_cube, max_drone_per_box):
    self.x_size = x
    self.y_size = y
    self.z_size = z
    self.max_drone_per_box = max_drone_per_box
    self.spaces = create_spaces(x, y, z, goal_cube, starting_cube)
    self.drone_factory = DroneFactory()
    self.starting_cube = self.spaces[starting_cube['x']][starting_cube['y']][starting_cube['z']]
    self.goal_cube = self.spaces[goal_cube['x']][goal_cube['y']][goal_cube['z']]

  def init_drones(self, num_drones):
    self.drones = []
    for _ in range(num_drones):
      drone = self.drone_factory.create_drone(self.starting_cube)
      self.drones.append(drone)

  def gen_solutions(self):
    self.routes = []
    for drone in self.drones:
      route = drone.fly_to(self.goal_cube, self.spaces)
      self.routes.append(route)

  def compute_score(self):
    pass








