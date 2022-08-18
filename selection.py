from random import uniform
from fitness import FitnessFunction
from parser import RcParser
from knapsack import KnapsackList
from parser import KnapsackParser, ItemParser
from item import ItemList


class RouletteSelection(object):

  def __init__(self, population):
    self.population = population
  def do_selection(self, items, rc):
    '''performs roulette selection'''
    fsum = 0
    pop_fsum = []
    for i in range(len(self.population)):
      fitness_function = FitnessFunction(self.population[i], items.decode_to_dict(self.population[i].solution), rc)
      fitness = fitness_function.get_minimun_profit()
      fsum = fsum + fitness 
      pop_fsum.append(fitness)
    # 轮盘赌
    bound = uniform(0, fsum)
    curr_fsum = 0
    for i in range(len(self.population)):
      curr_fsum = curr_fsum + pop_fsum[i]
      if curr_fsum >= bound:
        return self.population[i]
    
