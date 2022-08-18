if __name__ == '__main__':
    from parser import RcParser, ItemParser, KnapsackParser
    from chromosome import Chromosome
    from factory import ChromosomeFactory, PopulationFactory
    from crossover import OnePoint
    from item import ItemList
    from knapsack import KnapsackList
    from fitness import FitnessFunction
    from selection import RouletteSelection
    from population import Population
    from random import choice
    from mutation import Mutation
    from time import sleep
    from tqdm import tqdm
    import numpy as np
    rc = RcParser()
    n = rc.get_n()
    m = rc.get_m()
    # rc.get_rc_items获得对应的的item三元组(index, weight, profit)列表，再通过ItemParser得到实例化的Item对象，items是该对象的字段，代表items列表
    # ItemList同样拥有item列表，还有方法get_all_on_items，见内部注释
    items = ItemList(ItemParser(rc.get_rc_items()).items, m)
    # 背包对象组成的列表
    knapsacks = KnapsackList(KnapsackParser(rc.get_rc_knapsacks()).knapsacks)
    print(
        'please note that the number of iterations must be greater than or equal to the number of items'
    )
    print('number of knapsacks = {0}'.format(items.get_num_knapsack()))
    print('number of items = {0}'.format(n))

    p = 20
    print('population size = ' + str(p))
    # population拥有一个字段individual，是由chromosome对象组成的字符串，chromosome对象拥有字段solution，是该chromosome编码后的字符串
    population = PopulationFactory(p, n, m).gen()
    iterations = 4000
    print('iterations = {0}'.format(iterations))
    # sleep(0.5)
    fittest_chromosome = None
    # 每个迭代时最好的chromosome
    # TODO: 我们这需要max-min还是max profit？
    fittest_chromosomes = []
    max_min_chromosomes = []
    max_min = -1
    for _ in range(iterations):
        pop_fsum = 0  # 种群所有chromosome的profit之和
        #calc population sum
        # 遍历每个chromosome
        for i in range(p):
          # FitnessFunction为单个chromosome建立fitness函数，参数有该chromosome、decode得到的dict，具体方法见内部注释
            # fitness_function = FitnessFunction(
            #     population[i], items.get_all_on_items(population[i].solution,
            #                                           m), rc)
            fitness_function = FitnessFunction(
                population[i], items.decode_to_dict(population[i]), rc)

            pop_fsum = pop_fsum + fitness_function.sum_all_fitness()
            population[i] = fitness_function.chromosome  # 别忘了，因为repair了

        parents = []
        for i in range(2):  #select 2 chromosomes for crossover
            parent = RouletteSelection(population).do_selection(items, rc)
            parents.append(parent)

        point = choice(range(0, len(parents[0]), 4))

        children = OnePoint().exe(parents[0], parents[1], point)

        # 变异，概率为1/probability
        # 变异策略：若当前位点有归属则置零，否则随机选择一个背包放入
        # TODO 会变异出不可行解
        # TODO 对孩子变异？还是对种群随机选一个变异
        probability = 5
        mutated_children = []
        for i in range(2):
            mutated_children.append(Mutation(
                children[i], probability).exe())  #mutate offspring

        # if children be are better than parents, replace parents with children
        for i in range(2):
            fitness_function = FitnessFunction(mutated_children[i], items.decode_to_dict(mutated_children[i].solution), rc)
            # # minimum profit of this chromosome
            # if fitness_function.get_minimun_profit() < max_min:
            #   mutated_children[i] = parents[i]
            # else:
            #   max_min = fitness_function.get_minimun_profit()
            # print(len(mutated_children[i]), len(parents[i]))
            # if fitness_function.sum_all_fitness() < FitnessFunction(
            #         parents[i], items.decode_to_dict(parents[i].solution),
            #         rc).sum_all_fitness():
            #     mutated_children[i] = parents[i]
            # --- 上面的改成max-min ---#
            if fitness_function.get_minimun_profit() < FitnessFunction(
                    parents[i], items.decode_to_dict(parents[i].solution),
                    rc).get_minimun_profit():
                mutated_children[i] = parents[i]
            # else:
            #     population[i] = parents[i]

        for i, chromosome in enumerate(population): #replace current population with new one
          if str(chromosome) == str(parents[0]):
            population[i] = mutated_children[0]
          elif str(chromosome) == str(parents[1]):
            population[i] = mutated_children[1]

        #get list of fitness for each individual
        fsums = []
        max_min_list = []
        for i in range(p):
          fitness_function = FitnessFunction(population[i], items.decode_to_dict(population[i].solution), rc)
          fsums.append(fitness_function.sum_all_fitness() if fitness_function.is_all_feasible() else -1)
          max_min_list.append(fitness_function.get_minimun_profit())
        max_fsum = max(fsums)
        max_min = max(max_min_list)
          
        # for i in range(p):
        #   fitness_function = FitnessFunction(population[i], items.get_all_on_items(population[i].solution, m))
        #   fsums.append(fitness_function.sum_all_fitness())
        #   population[i] = fitness_function.chromosome

        # max_fsum = max(fsums)
        print(str(_))
        if max_fsum == -1:
            print('no feasible solution found')
        else:
            for i in range(p):
                if float(fsums[i]) == float(max_fsum):
                  fittest_chromosome = population[i]
                if float(max_min_list[i]) == float(max_min):
                  max_min_chromosome = population[i]
            fittest_chromosomes.append(fittest_chromosome)
            max_min_chromosomes.append(max_min_chromosome)
            # print('fittest solution from this population ' + str(fittest_chromosome) + ' where fsum = ' + str(max_fsum))
            print('max_sum: ', max_fsum)
            print('max_min: ', max_min)
            print('population fsum = ' + str(pop_fsum))
            it_best = items.get_all_on_items(fittest_chromosome, m)
            profit_list = []
            for k, v in it_best.items():
                print('{} {:<100}weight:{}\tprofit:{}'.format(
                    k, str([int(el.index / 4) for el in v]),
                    sum([el.weight for el in v]), sum([el.profit for el in v]),
                    np.var([el.profit for el in v])))
                profit_list.append(sum([el.profit for el in v]))
            print('variance of all knapsack:', np.var(profit_list))
    fittest_fsums = []
    for i in range(len(fittest_chromosomes)):
        fitness_function = FitnessFunction(
            fittest_chromosomes[i],
            items.decode_to_dict(fittest_chromosomes[i].solution), rc)
        fittest_fsums.append(fitness_function.sum_all_fitness())
        # TODO ?
        if i < p:
            population[i] = fitness_function.chromosome
    max_min_fsums = []
    for i in range(len(max_min_chromosomes)):
        fitness_function = FitnessFunction(
            max_min_chromosomes[i],
            items.decode_to_dict(max_min_chromosomes[i].solution), rc)
        max_min_fsums.append(fitness_function.get_minimun_profit())
        # TODO ?
        if i < p:
            population[i] = fitness_function.chromosome
    print('fittest fsums = ' + str(fittest_fsums))

    fittest_max_fsum = max(fittest_fsums)
    for i in range(len(fittest_fsums)):
        if float(fittest_fsums[i]) == float(fittest_max_fsum):
          final_chromosome = fittest_chromosomes[i]
        if float(fittest_max_fsum) == -1:
          print('no feasible solution found')
        else:
          final_max_min_chromosome = max_min_chromosomes[i]
    # print('fittest solutions from all populations \n \n' +
    #       str(Population(fittest_chromosomes)))
    #f_max_fsum = fitness_function.sum_all_fitness()
    #final_chromosome = fitness_function.chromosome
    # print('final fittest solution = ' + str(final_chromosome) +
    #       ', where fsum = ' + str(fittest_max_fsum))
    # result_knapsack = items.decode_to_dict(final_chromosome)

    print('final max_min_solution = '+', where fsum = ' + str(max_min_fsums))
    result_knapsack = items.decode_to_dict(final_max_min_chromosome)
    for k, v in result_knapsack.items():
        print('{} {:<100}weight:{}\tprofit:{}'.format(
            k, str([int(el.index / 4) for el in v]),
            sum([el.weight for el in v]), sum([el.profit for el in v])))
