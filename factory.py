from chromosome import Chromosome
from random import randint
from population import Population

class ChromosomeFactory(object):

  def __init__(self, n, m):
    self.n = n #number of items
    self.m = m #number of knapsacks
    self.item_vals = ['1', '0']
    self.knapsack_vals = [str(knapsack).zfill(3) for knapsack in range(0, m + 1)]

  def gen(self):
    '''generates a random chromosome'''
    def combine():
      return '0' + '000' if self.item_vals[randint(0, 1)] == '0' else '1' + self.knapsack_vals[randint(1, self.m)]
    return Chromosome(''.join([combine() for item_knapsack in range(self.n)]))


class PopulationFactory(object):

  def __init__(self, p, n, m):
    self.p = p #population size
    self.n = n #number of items
    self.m = m #number of knapsacks

  def gen(self):
    '''generates a population of size n'''
    f = ChromosomeFactory(self.n, self.m)
    return Population([f.gen() for i in range(self.p)])

