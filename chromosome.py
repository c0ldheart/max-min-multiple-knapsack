from util import gen_item_list, iseven

class Chromosome(object):

  def __init__(self, solution=None):
    self.solution = solution
  
  def __str__(self):
    return self.solution

  def __getitem__(self, key):
    '''given a key, returns a gene in this Chromosome'''
    return self.solution[key]

  def __setitem__(self, key, item):
    self.solution[key] = item

  def __len__(self):
    '''returns length of this Chromosome'''
    return len(self.solution)

  def __add__(self, p2):
    '''returns result of this Chromosome concatenated with p2'''
    return Chromosome(self.solution + str(p2))

    
         

