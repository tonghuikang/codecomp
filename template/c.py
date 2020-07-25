import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(grid):  # fix inputs here
    console("----- solving ------")
    # grid = [[int(a), int(b), c] for a,b,c in grid]

    n_planes = []
    s_planes = []
    w_planes = []
    e_planes = []

    for a,b,c in grid:
        a, b = int(a), int(b)
        if c == "U":
            n_planes.append((a,b))
        if c == "D":
            s_planes.append((a,b))
        if c == "L":
            w_planes.append((a,b))
        if c == "R":
            e_planes.append((a,b))
        
    console(n_planes)
    console(s_planes)
    console(w_planes)
    console(e_planes)

    # ns collision
    ns = collections.defaultdict(list)
    for a,b in n_planes:
        ns[a].append((b/2,1))
    for a,b in s_planes:
        ns[a].append((b/2,-1))
    
    ns = [(k,sorted(v)) for k,v in ns.items() if len(v) > 1 and len(set(x[1] for x in v)) == 2]
    console("ns", ns)

    # ew collision
    ew = collections.defaultdict(list)
    for a,b in w_planes:
        ew[b].append((a/2,-1))
    for a,b in e_planes:
        ew[b].append((a/2,1))

    ew = [(k,sorted(v)) for k,v in ew.items() if len(v) > 1 and len(set(x[1] for x in v)) == 2]
    console("ew", ew)

    # ne collision
    ne = collections.defaultdict(list)
    for a,b in n_planes:
        val = a+b
        ne[val].append((a,-1))
    for a,b in e_planes:
        val = a+b
        ne[val].append((a,1))

    ne = [(k,sorted(v)) for k,v in ne.items() if len(v) > 1 and len(set(x[1] for x in v)) == 2]
    console("ne", ne)

    # sw collision
    sw = collections.defaultdict(list)
    for a,b in s_planes:
        val = -a-b
        sw[val].append((a,1))
    for a,b in w_planes:
        val = -a-b
        sw[val].append((a,-1))

    sw = [(k,sorted(v)) for k,v in sw.items() if len(v) > 1 and len(set(x[1] for x in v)) == 2]
    console("sw", sw)

    # nw collision
    nw = collections.defaultdict(list)
    for a,b in n_planes:
        val = a-b
        nw[val].append((a,1))
    for a,b in w_planes:
        val = a-b
        nw[val].append((a,-1))

    nw = [(k,sorted(v)) for k,v in nw.items() if len(v) > 1 and len(set(x[1] for x in v)) == 2]
    console("nw", nw)

    # se collision
    se = collections.defaultdict(list)
    for a,b in s_planes:
        val = -a+b
        se[val].append((a,-1))
    for a,b in e_planes:
        val = -a+b
        se[val].append((a,1))

    se = [(k,sorted(v)) for k,v in se.items() if len(v) > 1 and len(set(x[1] for x in v)) == 2]
    console("se", se)

    minres = math.inf

    for c in [ns, ew, ne, sw, nw, se]:
        for _,v in c:
            # console(c)
            # console(v)
            for a,b in zip(v, v[1:]):
                # console(a)
                # console(b)
                if a[1] > b[1]:
                    # pass
                    minres = min(minres, b[0] - a[0])
    
    if minres == math.inf:
        return "SAFE"
    return int(minres*10)


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    nrows = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(input().split())

    res = solve(grid)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)