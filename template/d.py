import sys, os
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


# remove vertices with less than required edges until we find the answer :)
def solve_(edges, num_vertices, required):
    if required == 1:
        print(2)
        print(num_vertices)
        return
    if required == 2:
        print(2)
        print(*edges[0])
        return

    edges = [(a-1,b-1) for a,b in edges]
    # your solution here


    # fast modify, fast delete min, fast get min

    edge_count = Counter([])
    LARGE = 10**6
    for i in range(num_vertices):
        edge_count[i] += LARGE

    g = defaultdict(set)

    for a,b in edges:
        g[a].add(b)
        g[b].add(a)
        edge_count[a] -= 1
        edge_count[b] -= 1
    
    while edge_count:
        (k,v), = edge_count.most_common(1)
        if v <= LARGE - (required - 1):
            # console("starting", k)
            starting_node = k
            break
        
        for nex in g[k]:
            # g[k].remove(nex)
            g[nex].remove(k)
            # edge_count[k] += 1
            edge_count[nex] += 1
        del g[k]
        del edge_count[k]

    # check for all edges with exactly k-1 degree, if there is a clique
    # continue to remove

    # console(edge_count)
    if not edge_count:
        if len(edges) < (required*(required-1))//2:
            print(-1)
            return
        return

    stack = [starting_node]
    visited = [False for _ in range(num_vertices)]
    visited[starting_node] == True
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if visited[nex]:
                continue
            stack.append(nex)
            visited[nex] = True
    
    res = [i+1 for i,x in enumerate(visited)]
    print(1, len(res))
    print(*res)

    


def console(*args):  
    # print on terminal in different color
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
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
    # # screen input
    # if not ONLINE_JUDGE:
    #     console("----- solving ------")
    #     console(*args)
    #     console("----- ------- ------")
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
    # k = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    num_vertices, nrows, required = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    grid = []
    for _ in range(nrows):
        grid.append(list(map(int,input().split())))

    res = solve(grid, num_vertices, required)  # please change
    
    # print result
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)
    # print(*res)  # if printing a list