#!/usr/bin/env python3
import sys, getpass
import math, random, time
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly

end_time = time.time() + 1.8


# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
d4 = [(1,0),(0,1),(-1,0),(0,-1)]
dirs = ["D", "R", "U", "L"]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "hkmac"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    # if OFFLINE_TEST:
    #     log("----- solving ------")
    #     log(*args)
    #     log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# ---------------------------- template ends here ----------------------------


def solve_(sx, sy, trr, prr):
    # your solution here
    moore = [
        [1 , 2, 3, 6, 7,10,11,12],
        [64,63, 4, 5, 8, 9,14,13],
        [61,62,57,56,21,20,15,16],
        [60,59,58,55,22,19,18,17],
        [49,50,51,54,23,26,27,28],
        [48,47,52,53,24,25,30,29],
        [45,46,41,40,37,36,31,32],
        [44,43,42,39,35,34,34,33]
    ]
    moore = [[x-1 for x in row] for row in moore]
    moore = [[x//4 for x in row] for row in moore]

    regions = [[((i-1)//6, (j-1)//6) for i in range(50)] for j in range(50)]
    regions = [[(min(max(0,x),7),min(max(0,y),7)) for x,y in row] for row in regions]
    regions = [[moore[x][y] for x,y in row] for row in regions]
    start_region_tmp = regions[sx][sy]
    regions = [[(start_region_tmp-x)%64 for x in row] for row in regions]
    # start_region = regions[sx][sy]
    # log("start_region", start_region)

    # for row in regions:
    #     log(row)
    # assert False

    sx += 1
    sy += 1
    trr = [[-1] + row + [-1] for row in trr]
    prr = [[-1] + row + [-1] for row in prr]
    regions = [[-1] + row + [-1] for row in regions]
    trr = [[-1]*len(trr[0])] + trr + [[-1]*len(trr[0])]
    prr = [[-1]*len(prr[0])] + prr + [[-1]*len(prr[0])]
    regions = [[-1]*len(regions[0])] + regions + [[-1]*len(regions[0])]
    maxres = 0
    taken = set([-1, trr[sx][sy]])
    taken_arr = [-1, trr[sx][sy]]
    pos_arr = [(sx,sy)]
    pts_arr = [prr[sx][sy]]

    assert regions[sx][sy] == 0
    # log("start_region", start_region)
    curres = 0
    res_directions = []
    directions = []
    cx = sx
    cy = sy
    stuck_counter = 0

    while time.time() < end_time:
        while True:
            # print(cx,cy,taken,regions[cx][cy])
            # assert False
            idx = random.randint(0, 3)
            for i in range(idx, idx+4):
                i = i%4
                dx,dy = d4[i]
                xx = cx+dx
                yy = cy+dy
                if trr[xx][yy] in taken:
                    continue
                if not (regions[cx][cy] <= regions[xx][yy] <= regions[cx][cy] + 1):
                # if (regions[cx][cy]-1 <= regions[xx][yy] <= regions[cx][cy] + 1):
                    # if random.randint(1,100) < 0:
                    if stuck_counter < 100:
                    #     stuck_counter += 1
                        # log(regions[cx][cy], regions[xx][yy])
                        # stuck_counter += 1
                        # log("violate")
                        continue
                    # stuck_counter += 0
                    # stuck_counter = 0
                curres += prr[xx][yy]
                cx, cy = xx, yy
                directions.append(dirs[i])
                taken.add(trr[xx][yy])
                taken_arr.append(trr[xx][yy])
                pos_arr.append((xx,yy))
                pts_arr.append(prr[xx][yy])
                break
            else:  # dead end
                break
        
        if curres > maxres:
            res_directions = [x for x in directions]
            maxres = curres
            # log(maxres)
            stuck_counter = 0
        else:
            stuck_counter += 1
        
        # log(directions)
        for i in range(random.randint(1,40)):
            if directions:
                pos_arr.pop()
                directions.pop()
                taken.remove(taken_arr.pop())
                curres -= pts_arr.pop()
            else:
                break
        cx, cy = pos_arr[-1]
        # stuck_counter = 0
        # log(directions)
        # break
    
    # print(curres)

    return "".join(res_directions)


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    sx,sy = list(map(int,input().split()))
    # lst = list(map(int,input().split()))

    # read multiple rows
    trr = read_matrix(50)  # and return as a list of list of int
    prr = read_matrix(50)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(sx, sy, trr, prr)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)