import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


def solve_(edges, k):
    # your solution here
    d = defaultdict(list)

    for a,b in edges:
        d[a].append(b)
        d[b].append(a)

    c = Counter(len(v) for k,v in d.items())
    tails = [k for k,v in d.items() if len(v) == 1]
    junction = set([k for k,v in d.items() if len(v) >= 3])
    console(tails, junction)

    console(d)

    if c[1] == 0:  # one big circle
        return k*(k-1)
    
    if c[1] == 1:  # one tail
        cur = tails[0]
        visited = set([cur])
        tail_length = 0

        while not cur in junction:
            tail_length += 1
            for nex in d[cur]:
                if nex in visited:
                    continue
                visited.add(nex)
                cur = nex
                break
            # else:
            #     break

        console(tail_length)
        cycle_diameter = k - tail_length
        return cycle_diameter*(cycle_diameter-1) + tail_length*(2*cycle_diameter-1)


    cur = tails[0]
    visited = set([cur])
    tail_length = 0

    while not cur in junction:
        tail_length += 1
        for nex in d[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            cur = nex
            break
        # else:
        #     break

    junction_1 = cur
    tail_length_1 = tail_length

    visited.remove(cur)
    cur = tails[1]
    visited.add(cur)
    tail_length = 0

    while not cur in junction:
        tail_length += 1
        for nex in d[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            cur = nex
            break
        # else:
        #     break
    visited.remove(cur)

    junction_2 = cur
    tail_length_2 = tail_length

    console(tails[0], junction_1, tail_length_1)
    console(tails[1], junction_2, tail_length_2)

    cycle_diameter = k-tail_length_1-tail_length_2

    if junction_1 == junction_2:
        return cycle_diameter*(cycle_diameter-1) + tail_length_1*(2*cycle_diameter-1) + tail_length_2*(2*cycle_diameter-1) + tail_length_1*tail_length_2

    return cycle_diameter*(cycle_diameter-1) + tail_length_1*(2*cycle_diameter-1) + tail_length_2*(2*cycle_diameter-1) + 2*tail_length_1*tail_length_2



def console(*args):  
    # print on terminal in different color
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    pass


ONLINE_JUDGE = False

# if Codeforces environment
if os.path.exists('input.txt'):
    ONLINE_JUDGE = True

if ONLINE_JUDGE:
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

    def console(*args):
        pass


def solve(*args):
    # screen input
    if not ONLINE_JUDGE:
        console("----- solving ------")
        console(*args)
        console("----- ------- ------")
    return solve_(*args)


if True:
    # if memory is not a constraint
    inp = iter(sys.stdin.buffer.readlines())
    input = lambda: next(inp)
else:
    # if memory is a constraint
    input = sys.stdin.buffer.readline


for case_num in range(int(input())):
    # read line as a string
    # strr = input()

    # read line as an integer
    nrows = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    # lst = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid, nrows)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    print(res)
    # print(*res)  # if printing a list