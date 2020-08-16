import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

from intervaltree import IntervalTree

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lrr,wrr,hrr):  # fix inputs here
    console("----- solving ------")
    console("starts")
    console(lrr)
    console("widths")
    console(wrr)
    console("heights")
    console(hrr)

    tree = IntervalTree()
    coverage = 0
    heights = 0
    detours = 0

    result = []

    for l,w,h in zip(lrr,wrr,hrr):
        overlapping = tree.overlap(l-0.5, l+w+0.5)  # this is a set
        if len(overlapping) == 1:

            # edit tree
            interval = list(overlapping)[0] 
            tree.remove(interval)
            new_begin = min(interval.begin, l)
            new_end = max(interval.end, l+w)
            tree.addi(new_begin, new_end, interval.data)

            # edit calculations
            coverage += (new_end - new_begin) - (interval.end - interval.begin)
            heights += 0  # no change
            detours += 0  # no change

        elif len(overlapping) > 1:

            # edit tree
            tree.remove_overlap(l-0.5, l+w+0.5)
            begin_lst = [interval.begin for interval in overlapping]
            end_lst = [interval.end for interval in overlapping]
            data_lst = [interval.data for interval in overlapping]

            new_begin = min(min(begin_lst), l)
            new_end = max(max(end_lst), l+w)
            tree.addi(new_begin, new_end, max(data_lst))

            # edit calculations
            coverage += (new_end - new_begin) - sum([e-b for b,e in zip(begin_lst, end_lst)])
            heights += (max(data_lst) - sum(data_lst))  # decrease
            detours += sum([peak-h for peak in data_lst]) - (max(data_lst) - h)

        else:
            tree.addi(l, l+w, h)
            coverage += w
            heights += h

        console(coverage, heights, detours)
        res = coverage*2 + heights*2 + detours*2
        result.append(res)

    console(result)
    submission = 1
    for res in result:
        submission = submission*res%(10**9+7)

    return submission



    # return a string (i.e. not a list or matrix)
    return ""  


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

    res = solve(lrr,wrr,hrr)  # please change
    
    # Google - case number required
    print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
