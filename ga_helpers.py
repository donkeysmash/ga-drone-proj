
class Generation:
  def __init__(self, gen_id, prev_gen = None):
    self.gen_id = gen_id
    self.num_population = 0
    # self.best = None if prev_gen is None else prev_gen.best
    # self.second_best = None if prev_gen is None else prev_gen.second_best
    self.best = None
    self.second_best = None

  def add_population(self, solution):
    self.num_population += 1
    if self.best is None:
      self.best = solution
      return

    if self.second_best is None:
      self.second_best = solution
      return

    input_score = solution.score
    if input_score < self.best.score:
      self.second_best = self.best
      self.best = solution
      return

    if input_score < self.second_best.score:
      self.second_best = solution
      return



class Solution:
  def __init__(self, score, drones):
    self.score = score
    self.drones = drones


class GeneticAlgorithm:
  def __init__(self):
    self.generations = []

  def add_a_generation(self, generation):
    print('g{0}'.format(generation.gen_id))
    self.generations.append(generation)