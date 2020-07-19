import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(arr):  # fix inputs here
    console("----- solving ------")

    appear_once = False
    cnt = 0
    idxs = []

    for i,(a,b,c,d,e,f,g) in enumerate(zip(*[arr[i:] for i in range(7)])):
        if ((a == "a" or a == "?") and 
            (b == "b" or b == "?") and 
            (c == "a" or c == "?") and 
            (d == "c" or d == "?") and 
            (e == "a" or e == "?") and 
            (f == "b" or f == "?") and 
            (g == "a" or g == "?")):
            appear_once = True
            idxs.append(i)
        if a+b+c+d+e+f+g == "abacaba":
            cnt += 1
        
    console(arr)
    console(cnt, appear_once, idxs)

    if cnt > 1:
        print("No")
        return

    if not appear_once:
        print("No")
        return
    
    if cnt == 1:
        arr = arr.replace("?", "z")
        print("Yes")
        print(arr)
        return

    def count(brr):
        cnt = 0
        for i,(a,b,c,d,e,f,g) in enumerate(zip(*[brr[i:] for i in range(7)])):
            if a+b+c+d+e+f+g == "abacaba":
                cnt += 1
        console(brr, cnt)
        return cnt



    for idx in idxs:
        crr = "".join([x for x in arr[:idx]]) + "abacaba" + "".join([y for y in arr[idx+7:]])
    
        crr = crr.replace("?", "q")
        if count(crr) == 1:
            print("Yes")
            print(crr)
            return

    print("No")


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    strr = input()
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    _ = solve(strr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
