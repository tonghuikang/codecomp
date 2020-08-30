import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst, r1, r2, r3, d):  # fix inputs here
    console("----- solving ------")
    # console(lst, r1, r2, r3, d)
    # baseline = (len(lst)-1)*d + sum([x*r1 + r3 for x in lst])

    m1_cost = [r1*x + r3 for x in lst]       # shoot all, snipe boss, no relocation necessary
    m2_cost = [r2 + r1 + d for _ in lst]     # board clear, relocation necessary
    m3_cost = [r1*x + 2*r1 + d for x in lst]     # shoot all incl boss, relocation necessary

    m4_cost = [min(a,b) for a,b in zip(m2_cost, m3_cost)]

    baseline = sum(m1_cost) + (len(lst)-1)*d

    cost_diff = [a-b for a,b in zip(m1_cost, m4_cost)]

    # console("m1", m1_cost)
    # # console(m2_cost)
    # console("m4", m4_cost)
    # console(d, cost_diff)

    savings = [[0, -10**10] for _ in lst]
    savings[0][1] = max(cost_diff[0], -d)

    for i in range(1, len(lst)):
        savings[i][0] = max(0,  # reset
                            savings[i-1][0],   # no action
                            savings[i-1][1] + cost_diff[i],   # use outstanding
                            savings[i-1][1] - d)   # use outstanding and supplement, i.e. m1 only
        savings[i][1] = max(savings[i-1][0] + cost_diff[i],   # start outstanding
                            savings[i-1][0] - d)   # start outstanding with supplement

    total_savings = max(savings[-2][1], savings[-1][0])

    return baseline - total_savings


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()

for _ in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    # _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    _, r1, r2, r3, d = list(map(int,inp[0].split()))
    lst = list(map(int,inp[1].split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst, r1, r2, r3, d)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
