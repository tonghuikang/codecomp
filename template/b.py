import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve(lst):  # fix inputs here
    console("----- solving ------")

    console(lst)

    r = int("".join(lst), base=2)
    ones = bin(r).count("1")
    a = r%(ones-1)
    b = r%(ones)
    c = r%(ones+1)

    console(a,b,c)

    for i,x in enumerate(lst):
        # lst[i] = str(1-int(lst[i]))
        # x = int("".join(lst), base=2)
        if x == '1':
            y = ones-1
            z = (a + r ^ 1 << (len(lst) - i - 1))%(ones-1)
            if y == 0:
                print(0)
                continue
            if z == 0:
                print(1)
                continue
            console(z)
            cnt = 0
            while z != 0:
                y = z%y
                z = y
                cnt += 1

        if x == '0':
            y = ones+1
            z = (c + r ^ 1 << (len(lst) - i - 1))%(y)
            console(z)
            if z == 0:
                print(1)
                continue
            cnt = 0
            while z != 0:
                y = z%y
                z = y
                console(z, ones+1)
                cnt += 1
            
        # lst[i] = str(1-int(lst[i]))
        print(cnt)

    # return a string (i.e. not a list or matrix)
    return ""  


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


# for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
k = int(input())

    # read one line and parse each word as a string
lst = list(sys.stdin.readlines()[0])

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

res = solve(lst)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
