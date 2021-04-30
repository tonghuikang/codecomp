#!/usr/bin/env python3
import sys, getpass
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly
# sys.setrecursionlimit(10**6 + 5)

MAXINT = sys.maxsize

OFFLINE_TEST = False  # codechef does not allow getpass
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

# ---------------------------- template ends here ----------------------------


def solve_(krr,mrr,root,n):
    # your solution here
    default = krr[0]
    specials = set([x for x in krr])

    g = [set() for _ in range(n)]
    for a,b in mrr:
        g[a].add(b)
        g[b].add(a)

    distance = {}  # distance from root
    distance[root] = 0
    children = [set() for _ in range(n)]
    parent = {}

    stack = [root]
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in distance:
                continue
            stack.append(nex)
            children[cur].add(nex)
            parent[nex] = cur
            distance[nex] = distance[cur] + 1

    tagged_nodes_item = [-1 for _ in range(n)]
    for k in specials:
        tagged_nodes_item[k] = k

    leaves = set(i for i in range(n) if not children[i])

    # print(children)
    earliest = {}
    earliest[root] = 0

    while leaves:
        for cur in leaves:
            break
        # print(cur)
        leaves.remove(cur)
        if cur == root:
            break

        nex = parent[cur]
        if tagged_nodes_item[cur] != -1:
            tagged_nodes_item[nex] = tagged_nodes_item[cur]

        children[nex].remove(cur)
        if not children[nex]:
            leaves.add(nex)

    # print([tagged_nodes_item[i]  for i in range(n)])
    # print([distance[i]  for i in range(n)])
    # print([earliest[i]  for i in range(n)])


    stack = [root]
    while stack:
        cur = stack.pop()
        for nex in g[cur]:
            if nex in earliest:
                continue
            stack.append(nex)
            if tagged_nodes_item[nex] != -1:
                earliest[nex] = earliest[cur] + 1
            else:
                earliest[nex] = earliest[cur]
                tagged_nodes_item[nex] = tagged_nodes_item[cur]

    nodes = [tagged_nodes_item[i] for i in range(n)]
    nodes = [x if x!=-1 else default for x in nodes]

    vals = [2*earliest[i] - distance[i] for i in range(n)]
    # vals = [distance[i] if i in tagged_nodes else x for i,x in enumerate(vals)]

    nodes = [x+1 for x in nodes]
    return vals, nodes



# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # lst = input().split()
    
    # read one line and parse each word as an integer
    n,k,a = list(map(int,input().split()))
    krr = list(map(int,input().split()))
    krr = [x-1 for x in krr]

    # read multiple rows
    mrr = read_matrix(n-1)  # and return as a list of list of int
    mrr = [((a-1),(b-1)) for a,b in mrr]
    a -= 1
    # arr = read_strings(k)  # and return as a list of str

    res, res2 = solve(krr,mrr,a,n)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    print(" ".join(str(x) for x in res) + "\n" + " ".join(str(x) for x in res2))
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)