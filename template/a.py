import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def solve(n,k,w,
          lrr,al,bl,cl,dl,
          hrr,ah,bh,ch,dh):  # fix inputs here
    console("----- solving ------")
    console(n,k,w)
    # console(lrr)
    # console(al,bl,cl,dl)
    # console(hrr)
    # console(ah,bh,ch,dh)

    for _ in range(k, n):
        lrr.append(((al * lrr[-2] + bl * lrr[-1] + cl) % dl) + 1)
        hrr.append(((ah * hrr[-2] + bh * hrr[-1] + ch) % dh) + 1)
    
    console("bottom_left")
    console(lrr)
    console("width")
    console(w)
    console("heights")
    console(hrr)

    # ===== algorithm starts here =====
    # cumulative variables tracked
    height_changes = 0
    combed_blocks = 0

    corners = []  # [(-height, extent)]
    heapq.heapify(corners)
    
    cur_loc = 0
    cur_height = 0
    cur_block_start = lrr[0]

    result = []

    for l,h in zip(lrr,hrr):

        while corners and corners[0][1] < l:
            old_height, loc = heapq.heappop(corners)
            old_height = - old_height  # heapq correction
            if cur_loc <= loc:
                height_changes += cur_height - old_height
                cur_height = old_height
                cur_loc = loc
            if not corners:
                combed_blocks += cur_loc - cur_block_start
                height_changes += cur_height
            
        if not corners:  # broken and start new
            cur_block_start = l
            cur_height = 0

        if h > cur_height:
            height_changes += h - cur_height

        heapq.heappush(corners, (-h, l+w))

        cur_height = -corners[0][0]
        console(l,h,combed_blocks,cur_block_start,height_changes,cur_height,corners)
        res = (combed_blocks + l-cur_block_start+w)*2 + height_changes + cur_height
        result.append(res)

    console("result")
    console(result)

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    for l,h in list(zip(lrr,hrr))[::-1]:
        ax1.add_patch(  # DELETE
            patches.Rectangle((l, 0), w, h, ec="b"))
    plt.xlim(-1, max(lrr) + w + 1)
    plt.ylim(-1, max(hrr) + 1)
    plt.show()

    submission = 1
    for res in result:
        submission = submission*res%(10**9+7)


    # return a string (i.e. not a list or matrix)
    return submission


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
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
    n,k,w = list(map(int,input().split()))
    lrr = list(map(int,input().split()))
    al, bl, cl, dl = list(map(int,input().split()))
    hrr = list(map(int,input().split()))
    ah, bh, ch, dh = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(n,k,w,
                lrr,al,bl,cl,dl,
                hrr,ah,bh,ch,dh)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)


