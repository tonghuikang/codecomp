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

    anew = []
    for v,k in sorted([(v,k) for k,v in c1.items()])[::-1]:
        anew.extend([k]*v)

    bnew = [None for _ in arr]
    fallback_ptr = 0
    ptr = 0
    for a in anew:
        ptr = fallback_ptr
        while c2[a]:
            while anew[ptr] == a or bnew[ptr] != None:
                ptr += 1
                if ptr == len(arr):
                    ptr = fallback_ptr
            bnew[ptr] = a
            c2[a] -= 1
            ptr += 1
            if ptr == len(arr):
                ptr = fallback_ptr
            
            while bnew[fallback_ptr] != None:
                fallback_ptr += 1
                
    bremainder = []
    for k,v in c2.items():
        bremainder.extend([k] * v)

    console(c2)
    console(bnew)
    console(bremainder)

    for i in range(len(bnew)):
        if bnew[i] == None:
            bnew[i] = bremainder.pop()

    d = defaultdict(list)
    for a,b in zip(anew, bnew):
        d[a].append(b)
    
    console(anew)
    console(bnew)
    console(d)
    
    res = []
    for a in arr:
        b = d[a].pop()
        # assert b != a
        res.append(b)

    # assert(sorted(res) == sorted(brr))

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
