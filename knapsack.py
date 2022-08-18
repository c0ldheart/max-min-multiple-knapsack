class Knapsack(object):

  def __init__(self, capacity):
    self.capacity = capacity

  def __str__(self):
    return 'c = {0}'.format(self.capacity)


class KnapsackList(object):

  def __init__(self, knapsacks):
    self.knapsacks = knapsacks

  def __str__(self):
    return '\n'.join([str(knapsack) for knapsack in self.knapsacks])

  def __getitem__(self, key):
    return self.knapsacks[key]

  def __len__(self):
    return len(self.knapsacks)

