from universe import Universe

def run_simulation():
  num_generation = 150
  num_population = 50
  num_drones = 9

  limit = 10
  limit_x = limit
  limit_y = limit
  limit_z = limit

  maximum_drone_per_box = 3

  starting_cube = {'x': 0, 'y': 0, 'z': 0}
  goal_cube = {'x': 9, 'y': 9, 'z': 9}

  universe = Universe(limit_x, limit_y, limit_z, starting_cube, goal_cube, maximum_drone_per_box)
  for i in range(num_generation):
    universe.init_drones(num_drones)
    universe.gen_solutions()


if __name__ == '__main__':
  run_simulation()