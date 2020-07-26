import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr,brr):  # fix inputs here
    console("----- solving ------")
    console(arr)
    console(brr)


    abc = dict((ab, idx) for idx,ab in enumerate("abcdefghijklmnopqrst"))

    crr = []
    drr = []    
    for a,b in zip(arr,brr):
        if a > b:
            return -1
        if a != b:
            crr.append(abc[a])
            drr.append(abc[b])

    console(crr)
    console(drr)

    if len(crr) == 0:
        return 0

    d = defaultdict(set)

    for a,b in zip(crr,drr):
        d[a].add(b)
        d[b].add(a)

    console(d)
    visited = [False for _ in range(len(abc))]

    idx = 1

    for k in [x for x in d.keys()]:
        if visited[k]:
            continue
        idx += 1
        visited[k] = idx
        stack = [x for x in d[k]]
        while stack:
            cur = stack.pop()
            visited[cur] = idx
            # if not cur in d:
            #     continue
            for nex in d[cur]:
                if visited[nex]:
                    continue
                visited[nex] = idx
                stack.append(nex)
        console(d)

    console(visited)

    return sum([a-1 for a in Counter([x for x in visited if x]).values()])


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
    a = input()
    b = input()
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(a,b)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
