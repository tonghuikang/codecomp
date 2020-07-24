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

    abc = "abcdefghijklmnopqrstuvwxyz"
    abc = [x for x in abc]
    random.shuffle(abc)
    abc = "".join([str(x) for x in abc])

    cur = abc[-1] * 200 
    res = [cur]

    for i,a in enumerate(lst):
        nex = cur[:a] + abc[i%26]*(200-a)
        # print(nex)
        res.append(nex)
        cur = nex

    for r in res:
        print(r)

    # return a string (i.e. not a list or matrix)
    return None  


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
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

    solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
