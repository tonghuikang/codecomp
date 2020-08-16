import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

from intervaltree import IntervalTree

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

# import ray
# ray.init()

# @ray.remote
def solve(inp):  # fix inputs here
    lrr,wrr,hrr = inp
    console("----- solving ------")
    console("starts")
    console(lrr)
    console("widths")
    console(wrr)
    console("heights")
    console(hrr)

    coverage_tree = IntervalTree()
    vertical_tree = IntervalTree()
    coverage = 0
    heights = 0

    result = []

    delta = 0.5  # applied on input
    epsilon = 0.25  # applied to avoid null interval error
    MINVAL = -10**10
    MAXVAL =  10**10

    for idx,(l,w,h) in enumerate(zip(lrr,wrr,hrr)):

        # horizontal accounting
        overlapping = coverage_tree.overlap(l-delta, l+w+delta)  # this is a set
        if len(overlapping) == 0:
            coverage_tree.addi(l, l+w, None)
            coverage += w
        else:
            coverage_tree.remove_overlap(l-delta, l+w+delta)
            coverage -= sum([interval.end - interval.begin for interval in overlapping])
            new_begin = min(min(overlapping).begin, l)
            new_end = max(max(overlapping).end, l+w)
            coverage_tree.addi(new_begin, new_end, None)
            coverage += new_end - new_begin
        del overlapping

        # vertical accounting
        overlapping = vertical_tree.overlap(l-delta, l+w+delta)  # this is a set
        if len(overlapping) == 0:
            vertical_tree.addi(l,   l+epsilon,   (0,h, MAXVAL,l+w))
            vertical_tree.addi(l+w, l+w+epsilon, (0,h, l, MINVAL))
            heights += h*2

        else:
            vertical_tree.remove_envelop(l-delta, l+w+delta)
            for interval in overlapping:
                a,b,c,d = interval.data
                heights -= (b-a)
            
            left_interval = min(overlapping)
            right_interval = max(overlapping)

            if left_interval.begin == l and left_interval.data[3] != MINVAL:  # inherit everything
                left_pillar_start  = left_interval.data[0]
                left_pillar_extent = left_interval.data[2]
            elif left_interval.data[2] > l:
                left_pillar_start = 0
                left_pillar_extent = MAXVAL
            else:
                left_pillar_start  = left_interval.data[1]
                left_pillar_extent = left_interval.data[2]

            if right_interval.begin == l+w and right_interval.data[2] != MAXVAL:   # inherit everything
                right_pillar_start  = right_interval.data[0]
                right_pillar_extent = right_interval.data[3]
            elif right_interval.data[3] < l+w:
                right_pillar_start = 0
                right_pillar_extent = MINVAL
            else:
                right_pillar_start = right_interval.data[1]
                right_pillar_extent = right_interval.data[3]

            vertical_tree.addi(l,   l+epsilon,   (left_pillar_start, h, left_pillar_extent, l+w))
            vertical_tree.addi(l+w, l+w+epsilon, (right_pillar_start,h, l, right_pillar_extent))

            heights += h*2 - left_pillar_start - right_pillar_start

        res = coverage*2 + heights

        console("\n", idx+1, coverage, heights, res)
        console(coverage_tree)
        console(vertical_tree)

        result.append(res)

    console(result)
    submission = 1
    for res in result:
        submission = submission*res%(10**9+7)

    return submission



def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
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
    n,k = list(map(int,input().split()))
    lrr = list(map(int,input().split()))
    al, bl, cl, dl = list(map(int,input().split()))
    wrr = list(map(int,input().split()))
    aw, bw, cw, dw = list(map(int,input().split()))
    hrr = list(map(int,input().split()))
    ah, bh, ch, dh = list(map(int,input().split()))

    for _ in range(k, n):
        lrr.append(((al * lrr[-2] + bl * lrr[-1] + cl) % dl) + 1)
        wrr.append(((aw * wrr[-2] + bw * wrr[-1] + cw) % dw) + 1)
        hrr.append(((ah * hrr[-2] + bh * hrr[-1] + ch) % dh) + 1)

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ sin range(nrows):
    #     grid.append(list(map(int,input().split())))

    inputs.append([lrr,wrr,hrr])

# futures = [solve.remote(inp) for inp in inputs]
# results = ray.get(futures)

results = map(solve, inputs)

for case_num, res in enumerate(results):
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
