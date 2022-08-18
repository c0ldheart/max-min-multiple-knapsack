from parser import ItemParser, RcParser
from item import ItemList

def iseven(n): 
  return n % 2 == 0

def gen_item_list():
  return ItemList(ItemParser(RcParser().get_rc_items()).items)
