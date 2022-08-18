from operator import index


class Item(object):

  def __init__(self, index, profit, weight):
    self.index = index
    self.profit = profit
    self.weight = weight
    def __str__(self):
      return 'i = {0}, p = {1}, w = {2}'.format(self.index, self.profit, self.weight)

class ItemList(object):

  def __init__(self, items, num_knapsack):
    self.items = items
    self.num_knapsack = num_knapsack
  def __str__(self):
    return '\n'.join([str(item) for item in self.items])

  def __len__(self):
    return len(self.items)

  def __getitem__(self, key):
    '''given a key returns the associated item'''
    return self.items[key]

  def get_all_on_items(self, chromosome, m):
    '''returns on items with their associated knapsacks as dict of lists'''
    # chromosome是一个解编码后的字符串，m是int，代表背包个数，整个方法相当于将一串染色体解码，得到一个字典，key为背包index（从1开始），value是item对象组成的列表
    all_on_items = {}
    on_items = []
    # 遍历每个背包
    for knapsack in range(1, m + 1):
      #从染色体序列选择flag点后一位，也就是该交易归属平台的三位字符串的第一位（0xxx1xxx0xxx）
       for gene in range(1, len(chromosome), 4):
        # 选中一笔交易，判断是否属于当前背包，
         if chromosome[gene:gene+3] == str(knapsack).zfill(3):
            # 若属于当前背包，先获得该交易index，通过index获得item对象，再添加到当前背包item列表
            index = 0 if gene == 1 else ((gene - 1) / 4) -1 
            on_items.append(self.items[int(index)])
            # try:
            #   on_items.append(self.items[int(index)])
            # except:
            #   ValueError('index out of range')
            #   print('index = {0}, gene = {1}, knapsack = {2}'.format(index, gene, knapsack))
            #   exit()
       all_on_items[knapsack] = on_items
       on_items = []
    return all_on_items
    
  def decode_to_dict(self, chromosome):
      resut = dict([(key,[]) for key in range(1,self.num_knapsack+1)])
      for i in range(0, len(chromosome), 4):
        if chromosome[i] != '0':
          index_knapsack = int(chromosome[i+1:i+4])
          # print(index_knapsack, chromosome[i:i+4],[chromosome[i:i+4] for i in range(0, len(chromosome), 4)])
          resut[index_knapsack].append(self.items[int(i/4)])
      return resut

  def get_num_knapsack(self):
    return self.num_knapsack