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

    stack = [k]
    visited = {k: None}
    while stack:
        cur = stack.pop()
        for nex in d[cur]:
            if nex in visited:
                if visited[cur] == nex:
                    continue
                stack = []
                break
            visited[nex] = cur
            stack.append(nex)
    
    stack_1 = [cur]
    stack_1_set = set([cur])
    stack_2 = [nex]

    cur = stack_1[0]
    while visited[cur]:
        cur = visited[cur]
        stack_1.append(cur)
        stack_1_set.add(cur)
    

    cur = stack_2[0]
    while visited[cur]:
        cur = visited[cur]
        stack_2.append(cur)
        if cur in stack_1_set:
            break
    
    cycle = set(stack_2)
    for x in stack_1:
        if x in cycle:
            break
        cycle.add(x)


    # console("cycle", cycle)
    visited = set(cycle)

    res = k*(k-1)

    for start in cycle:
        stack = d[start]
        count = 0
        while stack:
            cur = stack.pop()
            if cur in cycle:
                continue
            visited.add(cur)
            # console(start, cur)
            count += 1
            for nex in d[cur]:
                if nex in visited:
                    continue
                stack.append(nex)
                visited.add(nex)
        console(start, count)
        res -= count*(count+1)//2

    return res

             



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