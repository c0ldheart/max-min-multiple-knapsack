import unittest
from crossover import OnePoint
from chromosome import Chromosome

class OnePointTest(unittest.TestCase):

  def test_exe(self):
    p1 = Chromosome("111100111100120000000013")
    p2 = Chromosome("000012131313111112001112")
    crossover_point = 4
    children = OnePoint().exe(p1, p2, crossover_point)
    expected_1 = Chromosome("111112131313111112001112")
    expected_2 = Chromosome("000000111100120000000013")
 
    self.assertEqual(children[0].solution, expected_1.solution) 
    self.assertEqual(children[1].solution, expected_2.solution)
