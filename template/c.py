import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    console("----- solving ------")
    console(lst)

    if sorted(lst) == lst:
        return "YES"

    minlst = min(lst)

    moveable_indexes = [i for i,x in enumerate(lst) if x%minlst==0]
    moveable_subsegment = [x for x in lst if x%minlst==0]

    moveable_subsegment = sorted(moveable_subsegment)

    lst2 = [x for x in lst]
    for i,j in enumerate(moveable_indexes):
        lst2[j] = moveable_subsegment[i]

    console(lst2)

    if sorted(lst2) == lst2:
        return "YES"
    return "NO"  


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
