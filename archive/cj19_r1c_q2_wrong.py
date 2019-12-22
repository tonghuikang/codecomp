#!/usr/bin/env python
import sys

str_input = input()
first_input = str_input.split()
t,f = [int(x) for x in first_input]  # 1 7 1000000
# 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 

dic = {"A":1, "B":2, "C":3, "D":4, "E":5}
inv_dic = {v: k for k, v in dic.items()}

for case_num in range(1, t+1):
    arr_all = []
    index_sets = [[5*x+1,5*x+2,5*x+3,5*x+4] for x in range(119)]
#     flatten = lambda l: [item for sublist in l for item in sublist]
#     indexes = flatten(indexes)
    recorded = []
    missing = []
    for indexes in index_sets:
        remainder = 1*2*3*4*5
        for index in indexes:
            print(index)
            sys.stdout.flush()
            str_input = input()     
            val = dic[str_input]
            recorded.append(val)
            remainder = int(remainder/val)
        missing.append(remainder)
    
    res = (inv_dic[360 - sum(recorded[0::4])] +
           inv_dic[360 - sum(recorded[1::4])] +
           inv_dic[360 - sum(recorded[2::4])] +
             inv_dic[360 - sum(recorded[3::4])] + 
             inv_dic[360 - sum(missing)])
        
    print(res)
    
#     for _ in range(n - 3):
#         print(("11 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18 18")) # 317
#         sys.stdout.flush()
#         dont_care = input()

#     print(result)
    sys.stdout.flush()
    result_which_we_dont_care = input()
    sys.stdout.flush()
    if result_which_we_dont_care == "N":
        print("exit")
        exit()