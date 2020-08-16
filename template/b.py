import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(n,k,lrr,al,bl,cl,dl,wrr,aw,bw,cd,dw,hrr,ah,bh,ch,dh):  # fix inputs here
    console("----- solving ------")
    console(n,k)
    # console(lrr)
    # console(al,bl,cl,dl)
    # console(wrr)
    # console(aw,bw,cw,dw)
    # console(hrr)
    # console(ah,bh,ch,dh)

    for _ in range(k, n):
        lrr.append(((al * lrr[-2] + bl * lrr[-1] + cl) % dl) + 1)
        wrr.append(((aw * wrr[-2] + bw * wrr[-1] + cw) % dw) + 1)
        hrr.append(((ah * hrr[-2] + bh * hrr[-1] + ch) % dh) + 1)

    console(lrr)
    console(wrr)
    console(hrr)

    # return a string (i.e. not a list or matrix)
    return ""  


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
    n,k = list(map(int,input().split()))
    lrr = list(map(int,input().split()))
    al, bl, cl, dl = list(map(int,input().split()))
    wrr = list(map(int,input().split()))
    aw, bw, cw, dw = list(map(int,input().split()))
    hrr = list(map(int,input().split()))
    ah, bh, ch, dh = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ sin range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(n,k,
                lrr,al,bl,cl,dl,
                wrr,aw,bw,cw,dw,
                hrr,ah,bh,ch,dh)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
