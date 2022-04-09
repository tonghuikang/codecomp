#!/usr/bin/env python3
import sys
import getpass  # not available on codechef
from collections import deque
input = sys.stdin.readline  # to read input quickly

# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

m9 = 10**9 + 7  # 998244353
yes, no = "YES", "NO"
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize
e18 = 10**18 + 10

# if testing locally, print to terminal with a different color
OFFLINE_TEST = getpass.getuser() == "htong"
# OFFLINE_TEST = False  # codechef does not allow getpass
def log(*args):
    if OFFLINE_TEST:
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

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

def minus_one(arr):
    return [x-1 for x in arr]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]

# ---------------------------- template ends here ----------------------------

# def dijkstra(list_of_indexes_and_costs, start):
#     # shortest path with nonnegative edge costs
#     # leetcode.com/problems/path-with-maximum-probability/
#     # leetcode.com/problems/network-delay-time/
#     length = len(list_of_indexes_and_costs)
#     visited = [False]*length
#     weights = [MAXINT]*length
#     path = [None]*length
#     queue = []
#     weights[start] = 0
#     heapq.heappush(queue, (0, start))
#     while queue:
#         g, u = heapq.heappop(queue)
#         if visited[u]:
#             continue
#         visited[u] = True
#         for v, w in list_of_indexes_and_costs[u]:
#             if not visited[v]:
#                 f = g + w
#                 if f < weights[v]:
#                     weights[v] = f
#                     path[v] = u
#                     heapq.heappush(queue, (f, v))
#     return path, weights


def solve_(mrr, e, w):

    for i in range(len(mrr)):
        while len(mrr[i]) < 3:
            mrr[i].append(0)

    # your solution here

    # def diff(arr, brr):
    #     # everything out and in
    #     res = len(arr) + len(brr)
    #     for a,b in zip(arr, brr):
    #         if a == b:
    #             # no need to take out
    #             res -= 2
    #     return res

    # states = [set() for _ in range(e)]
    # for i,lst in enumerate(mrr):
    #     arr = []
    #     for j,x in enumerate(lst):
    #         for _ in range(x):
    #             arr.append(j)

    #     combs = set()
    #     for comb in itertools.permutations(arr):
    #         combs.add(comb)
    #     states[i] = combs

    # g = [[] for _ in range(1680 * 11)]

    node_to_idx = {}
    idx_to_node = {}
    idx = 0

    def check_state(inp):
        stage, arr = inp[0], inp[1:]
        if stage == e:
            return inp
        a,b,c = mrr[stage]
        if arr.count(101) == a:
            if arr.count(102) == b:
                if arr.count(103) == c:
                    # log("up", (stage+1,) + arr)
                    return (stage+1,) + arr

        return inp
    
    start_node = (0,)
    end_node = (e,)

    node_to_cost = {}
    node_to_cost[start_node] = 0
    
    # def populate_to_get_idx(node):
    #     if node not in node_to_idx:
    #         idx += 1
    #         node_to_idx[cur] = idx
    #     return node_to_idx[cur]

    # start_idx = populate_to_get_idx(start_node)
    # end_idx = populate_to_get_idx(end_node)

    queue = deque([start_node])
    while queue:
        cur = queue.popleft()

        nex = check_state(cur)
        if nex not in node_to_cost:
            # log(nex)
            queue.append(nex)
            node_to_cost[nex] = node_to_cost[cur] + 1
            continue

        for addn in [101,102,103]:
            if cur[1:].count(addn) < 3:
                nex = cur + (addn,)
                if nex not in node_to_cost:
                    # log(nex)
                    queue.append(nex)
                    node_to_cost[nex] = node_to_cost[cur] + 1

        if len(cur) > 1:
            nex = cur[:-1]
            if nex not in node_to_cost:
                # log(nex)
                queue.append(nex)
                node_to_cost[nex] = node_to_cost[cur] + 1

    return node_to_cost[end_node] - e

    # for i,(prev_combs, next_combs) in enumerate(zip(states, states[1:]), start=1):

    #     a,b = mrr[i-1], mrr[i]
    #     base = sum(a) + sum(b)
    #     for x,y in zip(a,b):
    #         base -= min(x,y)/2
    #     log(base, a, b)

    #     for prev_comb in prev_combs:
    #         for next_comb in next_combs:
    #             cur = (i,) + prev_comb
    #             nex = (i+1,) + next_comb

    #             if cur not in node_to_idx:
    #                 idx += 1
    #                 node_to_idx[cur] = idx
    #             if nex not in node_to_idx:
    #                 idx += 1
    #                 node_to_idx[nex] = idx
    #             cur = node_to_idx[cur]
    #             nex = node_to_idx[nex]

    #             cost = diff(prev_comb, next_comb)

    #             if cost > base:
    #                 continue

    #             g[cur].append((nex, cost))
    
    # for comb in states[0]:
    #     cur = (0,)
    #     nex = (1,) + comb
    #     cost = len(comb)

    #     if cur not in node_to_idx:
    #         idx += 1
    #         node_to_idx[cur] = idx
    #     if nex not in node_to_idx:
    #         idx += 1
    #         node_to_idx[nex] = idx
    #     cur = node_to_idx[cur]
    #     nex = node_to_idx[nex]

    #     g[cur].append((nex, cost))

    # for comb in states[-1]:
    #     cur = (e,) + comb
    #     nex = (e+1,)
    #     cost = len(comb)

    #     if cur not in node_to_idx:
    #         idx += 1
    #         node_to_idx[cur] = idx
    #     if nex not in node_to_idx:
    #         idx += 1
    #         node_to_idx[nex] = idx
    #     cur = node_to_idx[cur]
    #     nex = node_to_idx[nex]

    #     g[cur].append((nex, cost))

    # start = node_to_idx[(0,)]
    # end = node_to_idx[(e+1,)]    
    # return dijkstra(g, start)[-1][end]


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    e,w = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    mrr = read_matrix(e)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(mrr,e,w)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    # print(res)
