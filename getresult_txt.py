import numpy as np

knapsack1 = [2, 3, 8, 9, 11, 19, 23, 29, 34, 48, 49]
knapsack2 = [0, 1, 20, 22, 36, 40, 42, 43, 45]
knapsack3 = [5, 12, 17, 21, 24, 26, 27, 33, 44, 47]
knapsack4 = [4, 6, 13, 16, 32, 37, 39, 41, 46]
knapsacks = []
[[20, 31, 35, 48, 50, 80, 88, 103, 141, 179, 192, 197]
2 [14, 49, 53, 61, 73, 82, 83, 91, 99, 133, 161, 172]
3 [1, 8, 21, 69, 74, 101, 102, 107, 137, 154, 187]
4 [27, 57, 62, 65, 112, 134, 142, 145, 151, 166, 185]
5 [7, 11, 15, 18, 19, 85, 89, 98, 139, 175, 198],
6 [12, 43, 70, 96, 105, 131, 155, 164, 169, 196],
7 [3, 4, 5, 13, 16, 56, 63, 71, 124, 144, 157, 159],
8 [9, 23, 28, 42, 104, 118, 149, 153, 174, 180, 183, 188, 193],
9 [17, 37, 39, 95, 97, 109, 115, 126, 132, 152, 177, 189],
10 [0, 22, 24, 32, 46, 51, 60, 92, 114, 123, 148, 182, 186],
# append all knapsack knapsacks
knapsacks.append(knapsack1)
knapsacks.append(knapsack2)
knapsacks.append(knapsack3)
knapsacks.append(knapsack4)

with open('result3.txt','w') as f:
    for _ in range(len(knapsacks)):
        for i in range(len(knapsacks[_])):
            line = str(knapsacks[_][i]+1) + "\n"
            f.write(line) 
        f.write('----------------------------------------------------------------\n')