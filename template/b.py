import sys
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict
import threading

# available on Google, not available on Codeforces
# import numpy as np
# import scipy
 
 
sys.setrecursionlimit(10**5+10)    # adjust numbers
threading.stack_size(1 << 27)     # for your needs


def solve(grid):  # fix inputs here
    console("----- solving ------")
    length = len(grid) + 1
 
    grid = [(a-1, b-1, c) for a,b,c in grid]
 
    
    g = defaultdict(list)
    
    for a,b,c in grid:
        g[a].append((b,c))
        g[b].append((a,c))
 
    console(g)
 
    global maxdist
    global maxnode
    global maxdist2
    global maxnode2
    global banned
    banned = set()
    maxdist, maxdist2 = 0, 0
    maxnode, maxnode2 = None, None
    visited = [False for _ in range(length)]  # don't need global lol
 
    def dfs(cur, dist):
        global maxdist
        global maxnode
        global maxdist2
        global maxnode2
        global banned
        if cur in banned:
            return
        console(cur, dist)
        if dist > maxdist:
            maxdist, maxdist2 = dist, maxdist
            maxnode, maxnode2 = cur, maxnode
        for nex, cost in g[cur]:
            if visited[nex]:  # dont go back
                continue
            visited[nex] = True
            dfs(nex, dist+cost)
            visited[nex] = False
 
    def reset():
        global maxdist
        global maxnode
        global maxdist2
        global maxnode2
        maxdist, maxdist2 = 0, 0
        maxnode, maxnode2 = None, None
        return
 
    # init
    console("res1")
    start_node = 0
    reset()
    visited[start_node] = True
    dfs(0, 0)
    console(start_node, banned)
    console(maxnode, maxdist)    
    console(maxnode2, maxdist2)    
 
    # save
    start_node_1 = maxnode
 
    # reset
    banned = set()
    console("res2")
    start_node = start_node_1
    reset()
    visited = [False for _ in range(length)]
    visited[start_node] = True
    dfs(start_node, 0)
    console(start_node, banned)
    console(maxnode, maxdist)    
    console(maxnode2, maxdist2)    
 
    # start_node_2 and start_node_1 are ends of the longest path. ban one of them
    console("best")
    res = [maxdist]
    start_node_2 = maxnode
    console(start_node_1, start_node_2)
    banned = set([start_node_1])
 
    console("res3")
    start_node = start_node_2
    reset()
    visited = [False for _ in range(length)]
    visited[start_node] = True
    dfs(start_node, 0)
    console(start_node, banned)
    console(maxnode, maxdist)    
    console(maxnode2, maxdist2)
    res.append(maxdist)
    res.append(maxdist2)
 
    banned = set([start_node_2])
 
    console("res3")
    start_node = start_node_1
    reset()
    visited = [False for _ in range(length)]
    visited[start_node] = True
    dfs(start_node, 0)
    console(start_node, banned)
    console(maxnode, maxdist)    
    console(maxnode2, maxdist2)
    res.append(maxdist)
    res.append(maxdist2)
 
    console(res)
 
    return sorted(res)[-2]
 
 
def console(*args):  # the judge will not read these print statement
    # print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return
 
# fast read all
# sys.stdin.readlines()
 
def main():
    # read line as a string
    # strr = input()
 
    # read line as an integer
    nrows = int(input())-1
    
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
 
    res = solve(grid)  # please change
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))
 
    # Codeforces - no case number required
    print(res)


main_thread = threading.Thread(target=main)
main_thread.start()
# main_thread.join()