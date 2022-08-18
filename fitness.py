from random import choice
import re
from chromosome import Chromosome
from item import ItemList
from parser import ItemParser

class FitnessFunction(object):

  def __init__(self, chromosome, knapsack_items_map, rc):
    self.chromosome = chromosome
    self.knapsack_items_map = knapsack_items_map
    self.rc = rc

  def sum_item_attribute(self, m_index, attribute):
    # 计算chromosome decode后，index=m的背包（从1开始）的profit sum和weight sum
    '''returns the sum of specified attribute of items in knapsacks m'''
    return sum([item.profit if attribute == 'profit' else item.weight for item in self.knapsack_items_map[m_index]])

  def get_minimun_profit(self):
    '''returns the minimum profit of this chromosome'''
    temp_min = 0x7fffffff
    for i in range(1, self.rc.get_m()+1):
      if self.sum_item_attribute(i, 'profit') < temp_min:
        temp_min = self.sum_item_attribute(i, 'profit')
    return temp_min

  def get_knapsack_capacity(self, m_index):
    '''returns capacity of knapsack m'''
    return self.rc.get_rc_knapsacks()[m_index]

  def sum_single_fitness(self, m_index):
    # 为第m_index背包计算profit_sum，如果该chromosome对于该背包为不可行解（物品总重量>背包容量），尝试修复他
    '''returns fitness of chromosomes in knapsack m'''
    if self.sum_item_attribute(m_index, 'weight') > self.get_knapsack_capacity(m_index - 1):
       self.random_repair(choice(range(1, len(self.chromosome), 4)), m_index)
    return self.sum_item_attribute(m_index, 'profit')

  def is_feasible(self, m):
    '''returns True if knapsack m is feasible'''
    return self.sum_item_attribute(m, 'weight') <= self.get_knapsack_capacity(m - 1)
  
  def is_all_feasible(self):
    '''returns True if all knapsacks are feasible'''
    for m in range(1, self.rc.get_m() + 1):
      if not self.is_feasible(m):
        return False
    return True

  def sum_all_fitness(self):
    '''returns total fitness of this chromosome'''
    fsum = 0
    for index_knapsack in range(1, self.rc.get_m() + 1):
      fsum = fsum + self.sum_single_fitness(index_knapsack)
    return fsum

  # def sum_all_fitness_with_variance(self):
  #   '''returns total fitness of this chromosome'''
  #   fsum = 0
  #   for knapsack in range(1, self.rc.get_m() + 1):
  #     fsum = fsum + self.sum_single_fitness(knapsack)
  #   average = fsum / self.rc.get_m()
  #   # get variance
  #   variance = 0
  #   for knapsack in range(1, self.rc.get_m() + 1):
  #     variance = variance + (self.sum_single_fitness(knapsack) - average) ** 2
  #   return 0.001 *(fsum - variance) if (fsum - variance) > 0 else 0

  # def sum_all_variance(self):
  #   '''returns total variance of this chromosome'''
  #   fsum = 0
  #   for knapsack in range(1, self.rc.get_m() + 1):
  #     fsum = fsum + self.sum_single_fitness(knapsack)
  #   average = fsum / self.rc.get_m()
  #   # get variance
  #   variance = 0
  #   for knapsack in range(1, self.rc.get_m() + 1):
  #     variance = variance + (self.sum_single_fitness(knapsack) - average) ** 2
  #   return variance

  def random_repair(self, i, m):
    '''transforms an infeasible solution into a feasible solution by random repair'''
    length = len(self.chromosome)
    # get chromosome's index that same as str(m).zfill(3)
    same_index = []
    for i in range(0, length, 4): 
      if self.chromosome[i+1:i+4] == str(m).zfill(3):
        same_index.append(i)
    i = choice(same_index)
    # while (self.chromosome[i:i+3] != str(m).zfill(3)): #find knapsack with exceeded capacity
    #   i = choice(range(1, length, 4))
    #   print('in while loop')
    # TODO 验证必然等于1
    if self.chromosome[i] == '1':
      c = Chromosome(self.chromosome[0:i] + '0000' + self.chromosome[i+4:])
      self.chromosome = c
      self.knapsack_items_map = ItemList(ItemParser(self.rc.get_rc_items()).items, self.rc.get_m()).decode_to_dict(c)
    else: 
      print('bug found!!!!')
      exit()

