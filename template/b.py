import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst, queries):  # fix inputs here
    console("----- solving ------")
    console(lst)
    console(queries)

    c = Counter(lst)

    counts = [0 for _ in range(9)]
    
    for k,v in c.items():
        if v > 8:
            v = 8
        counts[v] += 1

    console(counts)

    for a,b in queries:
        cur = c[b]
        if a == "+":
            c[b] += 1
        if a == "-":
            c[b] -= 1
        new = c[b]
    
        if cur > 8:
            cur = 8
        if new > 8:
            new = 8
        
        counts[cur] -= 1
        counts[new] += 1

        console(counts)

        if sum(counts[8:]) >= 1:
            print("YES")
            continue
        if sum(counts[6:]) >= 1 and sum(counts[2:]) >= 2:
            print("YES")
            continue
        if sum(counts[4:]) >= 2:
            print("YES")
            continue
        if sum(counts[4:]) >= 1 and sum(counts[2:]) >= 3:
            print("YES")
            continue    
        print("NO")

    # return a string (i.e. not a list or matrix)
    return


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
lines = sys.stdin.readlines()

# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
lst = list(map(int,lines[1].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))
num_queries = int(lines[2])

grid = [x.split() for x in lines[3:3+num_queries]]
grid = [(str(a), int(b)) for a,b in grid]

solve(lst, grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
