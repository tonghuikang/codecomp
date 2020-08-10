import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

def process(num):
    cnt_2 = 0
    cnt_5 = 0

    while num%2 == 0:
        num = num//2
        cnt_2 += 1
    
    while num%5 == 0:
        num = num//5
        cnt_5 += 1
    
    # return min(14,cnt_2-15), min(14,cnt_5-15)
    return cnt_2-9, cnt_5-9


def solve(lst):  # fix inputs here
    console("----- solving ------")

    grid = [[0 for _ in range(90)] for _ in range(90)]

    console(lst)
    for num in lst:
        x,y = process(num)
        console(x,y)
        grid[x+45][y+45] += 1
    # return a string (i.e. not a list or matrix)

    # console(np.array(grid))

    res = 0

    for i in range(-44,44):
        for j in range(-44,44):
            smaller_cnt = 0
            # smaller_cnt -= grid[10+i][10+j]
            for x in range(45-i,90):
                for y in range(45-j,90):
                    smaller_cnt += grid[x][y]
            # val = grid[10+i][10+j] * smaller_cnt + (grid[10+i][10+j] * (grid[10+i][10+j] - 1))
            if i >= 0 and j >= 0:
                val = grid[45+i][45+j] * (smaller_cnt - grid[45+i][45+j]) 
                val += (grid[45+i][45+j] * (grid[45+i][45+j]-1))
            else:
                val = (grid[45+i][45+j]) * smaller_cnt
            if val != 0:
                console(i,j,smaller_cnt,val)
            # val = max(0,val)
            res += val
    console(res)
    return res//2


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
lst = sys.stdin.readlines()

# for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # nrows = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
lst = [int(10**9 * float(x)) for x in lst[1:]]

res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
print(res)
