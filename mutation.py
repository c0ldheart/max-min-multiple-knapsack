from random import choice
from parser import RcParser
from chromosome import Chromosome
from random import randint

class Mutation(object):

  def __init__(self, chromosome, probability):
    self.chromosome = chromosome
    self.probabilty = probability
   
  def exe(self):
    for i in range(0, len(self.chromosome), 4):
      if choice(range(1, self.probabilty + 1)) == 1:
        if self.chromosome[i] == '1':
          return Chromosome(self.chromosome[:i] + '0000' + self.chromosome[i + 4:])
        elif self.chromosome[i] == '0':
            new_chromosome = self.chromosome[:i] + '1' + str(randint(1, RcParser().get_m())).zfill(3) + self.chromosome[i + 4:]
            # print('----', len(Chromosome(new_chromosome) ))
            return Chromosome(new_chromosome) 
    return self.chromosome

  
