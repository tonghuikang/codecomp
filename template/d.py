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

    d = defaultdict(set)
    for i,x in enumerate(lst):
        d[x].add(i)

    # console(d)

    res = []

    for i in range(len(lst)):
        if i == lst[i]:
            console(i, d)
            continue  # no changes necessary
        if d[i] == set():  # assign MEX
            res.append(i)
            d[lst[i]].remove(i)
            lst[i] = i
            d[lst[i]].add(i)  # not really necessary
            console(i, d)
            continue
        mex = 0
        while d[i]:
            idx = min(d[i])
            while d[mex] != set():
                mex += 1
            res.append(idx)
            d[i].remove(idx)
            lst[idx] = mex
            d[mex].add(idx)
        
        res.append(i)
        d[lst[i]].remove(i)
        lst[i] = i
        d[lst[i]].add(i)  # not really necessary
        console(i, d)

    return " ".join([str(x+1) for x in res])


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

cases = int(input())
inn = sys.stdin.readlines()

for case_num in range(cases):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,inn[2*case_num+1].split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve([x for x in lst])  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    cnt = [0 for _ in lst]

    console(lst)
    for i in res.split():
        i = int(i) - 1
        mex = len(lst)
        set_lst = set(lst)
        for x in range(len(lst)):
            if not x in set_lst:
                # console(x)
                mex = x
                break
        lst[i] = mex
        cnt[i] += 1
        console([x for x in lst])

    console(cnt)

    # Codeforces - no case number required
    console(len(lst)*2, len(res.split()))
    print(len(res.split()))
    print(res)
