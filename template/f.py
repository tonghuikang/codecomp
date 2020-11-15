import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

# assumption - the most common element remains the most common

def solve_(lst):
    # your solution here

    c = Counter(lst)

    if len(c) == 1:
        return 0
    
    a,b = c.most_common(2)
    if a[1] == b[1]:
        return len(lst)
    
    maxres = 0
    # counters = []
    for i,x in enumerate(lst):
        c[x] -= 1
        if c[x] == 0:
            del c[x]
        if len(c) == 1:
            break
        a,b = c.most_common(2)
        if a[1] == b[1]:
            maxres = max(maxres, len(lst)-i-1)
        # counters.append({k:v for k,v in c.items()})

    c = Counter(lst)
    for i,x in enumerate(lst[::-1]):
        c[x] -= 1
        if c[x] == 0:
            del c[x]
        if len(c) == 1:
            break
        a,b = c.most_common(2)
        if a[1] == b[1]:
            maxres = max(maxres, len(lst)-i-1)
    
    c = Counter(lst)
    (f,cnt), = c.most_common(1)
    poss = [i for i,x in enumerate(lst) if x == f] + [len(lst)]

    # console(poss)

    def frequency(x):
        maxres = 0
        # ptr_start = 0
        # ptr_end = poss[x+1]
        c = Counter(lst[poss[0]+1:poss[x+1]])
        # console(lst[poss[0]+1:poss[x+1]], c)

        if len(c) > 1:
            a,b = c.most_common(2)
            # console(a,b,"check",poss[x+1],poss[0])
            if a[1] == b[1]:
                maxres = max(maxres, poss[x+1]-poss[0]-1)

        for i,(start,end) in enumerate(zip(poss, poss[x+1:-1])):
            for remove in range(poss[i]+1, poss[i+1]+1):
                c[lst[remove]] -= 1
                if c[lst[remove]] == 0:
                    del c[lst[remove]]
            for add in range(poss[x+1+i], poss[x+2+i]):
                c[lst[add]] += 1
            
            # console(x, start, end, c)

            if len(c) > 1:
                a,b = c.most_common(2)
                if a[1] == b[1]:
                    maxres = max(maxres, poss[x+2+i]-(poss[i+1]+1))

        return maxres

    for x in range(max(2, cnt - 7), cnt):
        if x > cnt:
            continue
        fx = frequency(x)
        # console(x, fx)
        maxres = max(maxres, fx)

    return maxres


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    if not ONLINE_JUDGE:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    k = int(input())
    
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
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list