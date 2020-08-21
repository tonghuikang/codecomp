import sys
import heapq, functools, collections, itertools
import math, random
from collections import Counter, defaultdict

import collections,sys,threading
# threading.stack_size(2 ** 27)
# sys.setrecursionlimit(10**5 + 100)

# available on Google, not available on Codeforces
# import numpy as np
# import scipy

MOD = 10**9 + 7

# https://codeforces.com/blog/entry/80158?locale=en
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc


def solve(edges, fact):  # fix inputs here
    console("----- solving ------")
    fact = sorted(fact)[::-1]
    edges = [(a-1,b-1) for a,b in edges]
    total_nodes = len(edges) + 1

    console("og fact", fact)

    if len(fact) >= len(edges):
        pdt = 1
        for x in fact[:len(fact) - len(edges)+1]:
            pdt = (pdt*x)%MOD
        fact = [pdt] + fact[len(fact) - len(edges)+1:]

    console("check", total_nodes, fact, edges)

    if len(fact) <= len(edges):
        fact = fact + [1]*(len(edges) - len(fact))

    nodes = []
    for a,b in edges:
        nodes.extend([a,b])
    c = Counter(nodes)

    starting_leaf = sorted(c.items(), key=lambda x: x[1])[0][0]
    
    g = defaultdict(list)
    for a,b in edges:
        g[a].append(b)
        g[b].append(a)
    
    console(starting_leaf)

    assert len(g[starting_leaf]) == 1

    lst = [[1,total_nodes-1]]

    @bootstrap
    def dfs(cur, prev):
        if g[cur] == [prev]:
            console("leaf", cur)
            yield 1
        desc = 1
        for nex in g[cur]:
            if nex != prev:
                val = yield dfs(nex, cur)
                desc += val
                lst.append([total_nodes-val, val])

        yield desc

    # def dfs(cur, prev):
    #     if g[cur] == [prev]:
    #         console("leaf", cur)
    #         return 1
    #     desc = 1
    #     for nex in g[cur]:
    #         if nex != prev:
    #             val = (dfs(nex, cur))
    #             desc += val
    #             lst.append([total_nodes-val, val])

    #     return desc

    dfs(g[starting_leaf][0], starting_leaf)

    console(lst)
    console(fact)

    lst = sorted([a*b for a,b in lst])[::-1]
    console(lst)

    res = 0
    for a,b in zip(lst, fact):
        res += a*b
        res = res%MOD
    
    return res%MOD


def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

def main():
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
        for _ in range(nrows-1):
            grid.append(list(map(int,input().split())))

        _ = int(input())
        fact = list(map(int,input().split()))

        res = solve(grid, fact)  # please change
        
        # Google - case number required
        # print("Case #{}: {}".format(case_num+1, res))

        # Codeforces - no case number required
        print(res)

main()
# t = threading.Thread(target=main)
# t.start()
# t.join()