#!/usr/bin/env python3
import sys, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

# ---------------------------- template ends here ----------------------------

def alert(arr):
    print("! {} {}".format(len(arr), " ".join(str(x+1) for x in arr)), flush=True)

# -----------------------------------------------------------------------------


for case_num in range(int(input())):

    # read line as an integer
    if OFFLINE_TEST:
        n = 999
    else:
        n = int(input())

    if OFFLINE_TEST:
        impostors_simulated = set(random.sample(range(n), random.randint(n//3+1, 2*n//3-1)))
        log(impostors_simulated)

    @functools.lru_cache(maxsize=3000)
    def query_(a,b,c):
        if OFFLINE_TEST:
            if (a in impostors_simulated) + (b in impostors_simulated) + (c in impostors_simulated) > 1:
                return 0
            return 1

        print("? {} {} {}".format(a+1,b+1,c+1), flush=True)
        response = int(input())
        return response

    query_store = {}
    query_store_inv = {}

    def query(a,b,c):
        a,b,c = sorted([a,b,c])
        q = query_(a,b,c)
        query_store[a,b,c] = q
        query_store_inv[q] = (a,b,c)
        return q

    for a,b,c in zip(range(0,n,3), range(1,n,3), range(2,n,3)):
        q = query(a,b,c)

    assert len(query_store_inv) == 2

    a,b,c = query_store_inv[0]  # majority imp
    x,y,z = query_store_inv[1]  # majority cru

    log(query_store_inv)

    def check(a,b,c,x,y,z):
        possible = None
        for p1,p2,p3,p4,p5,p6 in itertools.product([0,1], repeat=6):
            for (p,pa),(q,pb),(r,pc) in itertools.combinations(zip([a,b,c,x,y,z], [p1,p2,p3,p4,p5,p6]), r=3):
                p,q,r = sorted([p,q,r])
                if (p,q,r) in query_store:
                    if query_store[p,q,r] == 1 and pa + pb + pc < 2:
                        break
                    if query_store[p,q,r] == 0 and pa + pb + pc > 1:
                        break
            else:
                if possible != None:  # already got another possibility
                    return False, None
                possible = [p1,p2,p3,p4,p5,p6]
        return True, possible

    query(a,b,z)
    query(a,y,c)
    query(x,b,c)

    query(x,y,c)
    query(x,b,z)
    query(a,y,z)

    query(a,b,y)
    query(a,x,c)
    query(z,b,c)

    boo, possible = check(a,b,c,x,y,z)

    assert boo

    res = {}
    res_inv = {}
    for abc, pos in zip([a,b,c,x,y,z], possible):
        res[abc] = pos
        res_inv[pos] = abc

    assert len(res_inv) == 2

    for abc in range(n):
        if abc not in res:
            q = query(res_inv[0], res_inv[1], abc)
            res[abc] = q

    log("res", res)

    impostors = []
    for k,v in res.items():
        if v == 0:
            impostors.append(k)

    impostors.sort()

    log(impostors)

    if OFFLINE_TEST:
        assert sorted(impostors) == sorted(impostors_simulated)
    alert(impostors)



sys.exit()
