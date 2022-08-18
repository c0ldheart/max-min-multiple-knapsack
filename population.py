class Population(object):

  def __init__(self, individuals):
    self.individuals = individuals
  
  def __str__(self):
    return ''.join([str(individual) + '\n' for individual in self.individuals])

  def __len__(self):
    return len(self.individuals)

  def __getitem__(self, key):
    return self.individuals[key]
  
  def __setitem__(self, key, item):
    self.individuals[key] = item
