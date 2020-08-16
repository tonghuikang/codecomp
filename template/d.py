import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

import ray
ray.init()

@ray.remote
def solve(inp):  # fix inputs here
    prr,qrr = inp
    console("----- solving ------")

    def attempt(x):
        cur = 0
        for p in prr:
            if p - qrr[cur] > x:  # cannot reach leftmost untouched, no longer possible
                return False
            
            if p > qrr[cur]:  # if going left
                extent = max(p,  # if not returning
                             p + x - 2*(p - qrr[cur]),  # if go left then go right
                             p + (x -   (p - qrr[cur]))//2
                            )   # if go right then go left
            else:
                extent = p + x
            
            # then go right and clear
            while qrr[cur] <= extent:
                cur += 1
                if cur == len(qrr):
                    return True
        return False

    # for tmp in range(70):
    #     if attempt(tmp):
    #         return tmp

    high = 2**32
    low = 0

    for _ in range(31):
        mid = (high + low)//2
        tmp = attempt(mid)
        # console(mid, attempt(mid))
        if tmp:
            high = mid
        else:
            low = mid
    
    for d in range(-5,5):
        tmp = mid+d
        if attempt(tmp):
            return tmp

    return mid


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

inputs = []


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    n,m,k,s = list(map(int,input().split()))
    prr = list(map(int,input().split()))
    al, bl, cl, dl = list(map(int,input().split()))
    qrr = list(map(int,input().split()))
    ah, bh, ch, dh = list(map(int,input().split()))

    for _ in range(k, n):
        prr.append(((al * prr[-2] + bl * prr[-1] + cl) % dl) + 1)

    for _ in range(k, m):
        qrr.append(((ah * qrr[-2] + bh * qrr[-1] + ch) % dh) + 1)

    # prr = [-x for x in prr]
    # qrr = [-x for x in qrr]
    prr = sorted(prr)
    qrr = sorted(qrr)
    console(prr)
    console(qrr)

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    inputs.append([prr,qrr])

futures = [solve.remote(inp) for inp in inputs]
results = ray.get(futures)

for case_num, res in enumerate(results):
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
