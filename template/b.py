import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr, brr):  # fix inputs here
    console(arr)
    console(brr)
    console("----- solving ------")
    c1 = Counter(arr)
    c2 = Counter(brr)

    for k,v in c1.items():
        if k in c2:
            if v + c2[k] > len(arr):
                print("No")
                return

    anew = sorted(arr)
    bnew = sorted(brr)[::-1]

    idxs = set([i for i,(a,b) in enumerate(zip(anew,bnew)) if a == b])
    swaps = []

    if idxs:
        same_num = bnew[list(idxs)[0]]
        for i in range(len(arr)):
            if i in idxs:
                continue
            if bnew[i] == same_num:
                continue
            if anew[i] == same_num:
                continue
            swaps.append(i)
            if len(swaps) == len(idxs):
                break
    
    assert len(swaps) == len(idxs)
    
    console()
    console(anew)
    console(bnew)
    console(idxs)
    console(swaps)
    console()

    for x,y in zip(swaps, idxs):
        bnew[x], bnew[y] = bnew[y], bnew[x]

    d = defaultdict(list)
    for a,b in zip(anew, bnew):
        d[a].append(b)
    
    
    res = []
    for a in arr:
        b = d[a].pop()
        assert b != a
        res.append(b)

    # assert(sorted(res) == sorted(brr))

    console()
    console(anew)
    console(bnew)
    console(idxs)
    console(swaps)
    console()

    print("Yes")
    print(" ".join([str(a) for a in res]))

    return





def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(arr, brr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
