import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np    # PLEASE DISABLE
# import scipy


def solve(grid,w,h):  # fix inputs here
    console("----- solving ------")
    console(grid)
    console(w,h)

    dl = collections.defaultdict(list)
    dr = collections.defaultdict(list)

    for i,row in enumerate(grid):
        for j,cell in enumerate(row):
            dl[i+j].append(cell)
            dr[i-j].append(cell)

    console(sorted(dl.items()))
    console(sorted(dr.items()))

    dl_cnt = collections.defaultdict(list)
    dr_cnt = collections.defaultdict(list)
    dl_rev_cnt = collections.defaultdict(list)
    dr_rev_cnt = collections.defaultdict(list)

    for k,v in dl.items():
        cnt = 1
        prev = None
        for x in v:
            if x == prev:
                cnt += 1
            else:
                cnt = 1
            prev = x
            dl_cnt[k].append(cnt)

        cnt = 1
        prev = None
        for x in v[::-1]:
            if x == prev:
                cnt += 1
            else:
                cnt = 1
            prev = x
            dl_rev_cnt[k].append(cnt)
            
    for k,v in dr.items():
        cnt = 1
        prev = None
        for x in v:
            if x == prev:
                cnt += 1
            else:
                cnt = 1
            prev = x
            dr_cnt[k].append(cnt)

        cnt = 1
        prev = None
        for x in v[::-1]:
            if x == prev:
                cnt += 1
            else:
                cnt = 1
            prev = x
            dr_rev_cnt[k].append(cnt)

    console("dl_cnt", sorted(dl_cnt.items()))
    console("dr_cnt", sorted(dr_cnt.items()))
    console("dl_rev_cnt", sorted(dl_rev_cnt.items()))
    console("dr_rev_cnt", sorted(dr_rev_cnt.items()))

    grid_dl = [[None for _ in range(w)] for _ in range(h)]
    grid_dr = [[None for _ in range(w)] for _ in range(h)]
    grid_dl_rev = [[None for _ in range(w)] for _ in range(h)]
    grid_dr_rev = [[None for _ in range(w)] for _ in range(h)]

    for k,v in sorted(dl_cnt.items()):
        i = max(0, k-h+1)
        j = min(w-1, k)
        print(k,i,j,v)
        for x in v:
            grid_dl[i][j] = x
            i, j = i+1, j-1

    console()

    for k,v in sorted(dl_rev_cnt.items()):
        i = max(0, k-h+1)
        j = min(w-1, k)
        print(k,i,j,v)
        for x in v[::-1]:
            grid_dl_rev[i][j] = x
            i, j = i+1, j-1

    console()

    for k,v in sorted(dr_cnt.items()):
        if k <= 0:
            i,j = -k,0
        else:
            i,j = 0,k
        print(k,i,j,v)
        for x in v:
            grid_dr[i][j] = x
            i, j = i+1, j+1

    console()

    for k,v in sorted(dr_rev_cnt.items()):
        if k <= 0:
            i,j = -k,0
        else:
            i,j = 0,k
        print(k,i,j,v)
        for x in v[::-1]:
            grid_dr_rev[i][j] = x
            i, j = i+1, j+1

    # PLEASE DISABLE
    # console(np.array(grid_dl))
    # console()
    # console(np.array(grid_dr))
    # console()
    # console(np.array(grid_dl_rev))
    # console()
    # console(np.array(grid_dr_rev))

    maxx = [[None for _ in range(w)] for _ in range(h)]

    for i in range(h):
        for j in range(w):
            maxx[i][j] = min(grid_dl[i][j], grid_dr[i][j], grid_dl_rev[i][j], grid_dr_rev[i][j])


    # return a string (i.e. not a list or matrix)
    return sum(sum(row) for row in maxx)


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
h, w = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
grid = []
for _ in range(h):
    # grid.append(list(map(int,input().split())))
    grid.append(list(input()))

res = solve(grid,w,h)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
print(res)
