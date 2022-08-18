from os.path import abspath
import yaml
from yaml import safe_load
from item import Item
from knapsack import Knapsack

class RcParser(object):
  def __init__(self):
   with open(abspath('excel_data1.yaml'), 'r') as ymlf:
     self.rc = safe_load(ymlf.read())
  
  def __str__(self):
    return str(self.rc) 

  def get_rc_items(self):
    '''returns a list of a list of items'''
    return self.rc['items']
  
  def get_rc_knapsacks(self):
    '''returns a list of knapsacks'''
    return self.rc['knapsacks']

  def get_n(self):
    '''returns n, the number of items'''
    return self.rc['n']

  def get_m(self):
    '''returns m, the number of knapsacks'''
    return self.rc['m']

class ItemParser(object):

  def __init__(self, items):
    self.items = [Item(*item) for item in items]

  def __str__(self):
    return ''.join([str(item) + '\n' for item in self.items])

class KnapsackParser(object):

  def __init__(self, knapsacks):
    self.knapsacks = [Knapsack(knapsack) for knapsack in knapsacks]

  def __str__(self):
    return ''.join([str(knapsack) + '\n' for knapsack in self.knapsacks])

