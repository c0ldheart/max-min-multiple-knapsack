from util import iseven
from chromosome import Chromosome

class OnePoint(object):

  def exe(self, p1, p2, i):
    '''applies one point crossover to p1 and p2 returning 2 offspring, i is the crossover point and must be even'''
    if iseven(i):
      return [Chromosome(p1[:i] + p2[i:]), Chromosome(p2[:i] + p1[i:])]
    else: 
      raise(ValueError('crossover point must be even'))
 
 
