#!/usr/bin/env python3
import sys
from collections import defaultdict, deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout

# if testing locally, print to terminal with a different color
OFFLINE_TEST = False
CHECK_OFFLINE_TEST = True
# CHECK_OFFLINE_TEST = False  # uncomment this on Codechef
if CHECK_OFFLINE_TEST:
    import getpass
    OFFLINE_TEST = getpass.getuser() == "htong"

def log(*args):
    if CHECK_OFFLINE_TEST and OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

# ---------------------------- template ends here ----------------------------


def binary_lifting_preprocessing(graph, start_node):
    """graph: map or list of node to nodes"""

    ancestors_binary = defaultdict(list)
    visited = set([start_node])
    queue = deque([start_node])

    while queue:
        cur = queue.popleft()
        for nex in graph[cur]:
            if nex in visited:
                continue
            ancestors_binary[nex].append(cur)

            anc = cur
            idx = 0
            while len(ancestors_binary[anc]) >= len(ancestors_binary[nex]):
                ancestors_binary[nex].append(ancestors_binary[anc][idx])
                anc = ancestors_binary[anc][idx]
                idx += 1
            
            queue.append(nex)
            visited.add(nex)

    return ancestors_binary


def binary_lifting_query(node, height, ancestors_binary):
    # assumes that the node is at least height deep
    idx = 0
    while height:
        if height&1:
            node = ancestors_binary[node][idx]
        else:
            pass
        height = height >> 1
        idx += 1
    return node


for case_num in [0]:  # no loop over test case
    # your solution here
    n = int(input())
    g = defaultdict(list)
    for a,b in read_matrix(n-1):
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    queue = deque([0])
    visited = set([0])
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in visited:
                continue
            queue.append(nex)
            visited.add(nex)
        
    log(cur)
    start = cur

    queue = deque([start])
    visited = set([start])
    while queue:
        cur = queue.popleft()
        for nex in g[cur]:
            if nex in visited:
                continue
            queue.append(nex)
            visited.add(nex)
        
    end = cur
    log(end)

    a1 = binary_lifting_preprocessing(g, start)
    a2 = binary_lifting_preprocessing(g, end)

    allres = []
    q = int(input())
    for a,b in read_matrix(q):
        a -= 1
        res = -2
        try:
            res = max(res, binary_lifting_query(a,b,a1))
        except IndexError:
            pass
        try:
            res = max(res, binary_lifting_query(a,b,a2))
        except IndexError:
            pass
        allres.append(res)

    print("\n".join(str(x+1) for x in allres))

