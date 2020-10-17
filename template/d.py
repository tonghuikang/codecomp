import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(lst):
    # your solution here

    cnt = [0,0,0,0]
    arr = [[],[],[],[]]

    single_1 = []
    single_2 = []
    single_3 = []
    pairs_2 = []
    pairs_3 = []
    pairs_3_above = []

    i = len(lst)
    for a in lst[::-1]:
        i -= 1

        # check feasible
        cnt[a] += 1

        # console(single_1)
        if a == 1:
            single_1.append(i)
        if a == 2:
            if single_1:
                pairs_2.append((i, single_1.pop()))
                single_2.append(i)
            else:
                print(-1)
                return
        if a == 3:
            if single_2:
                pairs_3_above.append((i, single_2.pop()))
                single_2.append(i)
            elif single_1:
                pairs_3.append((i, single_1.pop()))
                single_2.append(i)
            else:
                print(-1)
                return

    # console(single_1)
    # console(pairs_2)
    # console(pairs_3)

    cur = 0
    res = []

    for a,b in pairs_3_above[::-1]:
        cur += 1
        res.append((a,cur))
        res.append((b,cur))

    for a,b in pairs_2:
        cur += 1
        res.append((a,cur))
        res.append((b,cur))
    
    for a,b in pairs_3:
        cur += 1
        res.append((a,cur))
        res.append((b,cur))
        cur += 1
        res.append((b,cur))

    for a in single_1:
        cur += 1
        res.append((a,cur))

    # console(res)
    
    if res:
        c_check_x = Counter()
        c_check_y = Counter()
        for a,b in res:
            c_check_x[a] += 1
            c_check_y[b] += 1
        assert max(c_check_x.values()) <= 2
        assert max(c_check_y.values()) <= 2
        assert max(c_check_x) <= len(lst)
        assert max(c_check_y) <= len(lst)

    cout = [str(len(res))]
    for a,b in res:
        cout.append("{} {}".format(b,a+1))
    print("\n".join(cout))
    return


def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


# if Codeforces environment
if os.path.exists('input.txt'):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    console("----- solving ------")
    # console(*args)
    console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in [1]:
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    res = solve(lst)  # please change
    
    # post processing methods
    # if res != [-1]:
    #     print(len(res))
    # res = [str(x) for x in res]
    # res = " ".join(res)

    # # print result
    # # Google - case number required
    # # print("Case #{}: {}".format(case_num+1, res))

    # # Codeforces - no case number required
    # print(res)