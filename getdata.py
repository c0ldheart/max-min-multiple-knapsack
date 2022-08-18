import yaml
import numpy as np
weight_list = []
profit_list = []

# read txt
with open('data.txt', 'r') as f:
    for line in f:
        line = line.strip()
        line = line.split()
        weight_list.append(int(line[0]))
        profit_list.append(int(line[1]))

# print(weight_list, profit_list)

target_data = {}
# to yaml
target_data['items'] = []

for i in range(len(weight_list)):
    target_data['items'].append([i * 4, profit_list[i], weight_list[i]])

target_data['knapsacks'] = [800] * 20
target_data['m'] = len(target_data['knapsacks'])
target_data['n'] = len(weight_list)
print(target_data)

with open('excel_data4.yaml', 'w') as f:
    yaml.dump(target_data, f)
