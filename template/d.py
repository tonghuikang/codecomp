import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy




def solve(lst):  # fix inputs here
    console("----- solving ------")
    global cout
    cout = []
    status = [x for x in lst]

    def print(strr):
        global cout
        cout += [strr]

    # if sum(lst) % len(lst) != 0:
    #     print(-1)
    #     return "\n".join(str(x) for x in cout)
    
    if len(set(lst)) == 1:
        cout = []
        print(0)
        return "\n".join(str(x) for x in cout)

    target = sum(lst) // len(lst)


    # sort by distance to fulfillment
    arr = sorted([((-x)%i,x,i) for i,x in enumerate(lst, start=1)])

    assert arr[0][2] == 1

    for remaining_to_fulfill, x, i in arr[1:]:
        if status[0] <= remaining_to_fulfill:  # you cannot already
            break
        print("{} {} {}".format(1, i, remaining_to_fulfill))
        status[0] -= remaining_to_fulfill
        status[i-1] += remaining_to_fulfill

        multiple = status[i-1]//i
        print("{} {} {}".format(i, 1, multiple))
        status[0] += multiple*i
        status[i-1] -= multiple*i
        # assert status[i-1] == 0
        
    console(status)

    # transfer all equally    
    for i,x in enumerate(status[1:], start=2):
        transfer = target-x
        print("{} {} {}".format(1, i, transfer))
        status[0] -= transfer
        status[i-1] += transfer

    console(status)

    if len(set(status)) != 1:
        cout = []
        print(-1)
        return "\n".join(str(x) for x in cout)

    # return a string (i.e. not a list or matrix)
    return "\n".join(str(x) for x in [len(cout)] + cout)


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
inp = sys.stdin.readlines()
currow = 0

for case_num in range(int(inp[0])):
    # read line as a string
    # strr = input()

    # read line as an integer
    # k = int(input())
    currow += 2

    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    lst = list(map(int,inp[currow].split()))

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
    print(res)
