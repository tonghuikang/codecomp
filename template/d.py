import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(prr,qrr):  # fix inputs here
    console("----- solving ------")

    def attempt(x):
        cur = 0
        for p in prr:
            if p - qrr[cur] > x:  # cannot reach leftmost untouched, no longer possible
                return False
            
            if p > qrr[cur]:  # if going left
                remainder = max(0, x - 2*(p - qrr[cur])) # how much time left after reaching leftmost of untouched
            else:
                remainder = x
            # console(p, remainder)
            
            # then go right and clear
            extent = p+remainder
            while qrr[cur] <= extent:
                cur += 1
                if cur == len(qrr):
                    return True
        return False

    # for tmp in range(30):
    #     if attempt(tmp):
    #         return tmp

    high = 2**31
    low = 0

    for _ in range(31):
        mid = (high + low)//2
        tmp = attempt(mid)
        # console(mid, attempt(mid))
        if tmp:
            high = mid
        else:
            low = mid
    
    for d in range(-2,2):
        tmp = mid+d
        if attempt(tmp):
            return tmp

    return mid


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

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

    console(prr)
    console(qrr)
    prr = sorted(prr)
    qrr = sorted(qrr)

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(prr,qrr)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
