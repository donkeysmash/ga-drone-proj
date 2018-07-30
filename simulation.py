from universe import Universe
from ga_helpers import Generation, Solution, GeneticAlgorithm

def run_simulation():
  num_generation = 10
  num_population = 10
  num_drones = 9

  limit = 10
  limit_x = limit
  limit_y = limit
  limit_z = limit

  maximum_drone_per_box = 3

  p_c = 0.6
  p_m = 0.25
  alpha = 0.5

  collision_penalty = 10000

  starting_cube = {'x': 0, 'y': 0, 'z': 0}
  goal_cube = {'x': 9, 'y': 9, 'z': 9}

  my_ga = GeneticAlgorithm()

  universe = Universe(limit_x, limit_y, limit_z, starting_cube, goal_cube, maximum_drone_per_box, p_c, p_m, alpha)
  very_first_generation = Generation(0)
  for _ in range(num_population):
    universe.reset()
    universe.init_drones(num_drones)
    universe.gen_solutions()
    universe.compute_cost_and_collision()
    score = universe.compute_score(collision_penalty)
    a_solution = Solution(score, universe.drones)
    very_first_generation.add_population(a_solution)
  my_ga.add_a_generation(very_first_generation)

  for i in range(1, num_generation):
    prev_generation = my_ga.generations[i - 1]
    generation = Generation(i, prev_generation)
    for _ in range(num_population):
      universe.reset()
      universe.init_drones(num_drones)
      universe.gen_children(prev_generation.best, prev_generation.second_best)
      universe.compute_cost_and_collision()
      score = universe.compute_score(collision_penalty)
      a_solution = Solution(score, universe.drones)
      generation.add_population(a_solution)
    my_ga.add_a_generation(generation)

  import pdb; pdb.set_trace()

if __name__ == '__main__':
  run_simulation()