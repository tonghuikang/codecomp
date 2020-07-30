import sys, threading
import heapq, functools, collections
import math, random
from collections import Counter, defaultdict, deque

# available on Google, not available on Codeforces
# import numpy as np
# import scipy


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


def solve(arr, brr):  # fix inputs here
    console("----- solving ------")
    # arr value
    # brr parent

    # get children
    g = defaultdict(list)
    for i,b in enumerate(brr, start=1):
        g[b].append(i)
    
    # console(g)

    p = {}  # maximum value of subtree
    q = defaultdict(list) # children of maximum value of subtree
    # other_roots = set()

    @bootstrap
    def get_maximum_subtree_children(node):
        node_val = arr[node-1]
        
        if g[node] == []:
            p[node] = node_val
            yield node_val

        for nex in g[node]:
            child_val = yield get_maximum_subtree_children(nex)
            if child_val > 0:
                q[node].append(nex)
                node_val += child_val
            # else:
            #     other_roots.add(nex)
        p[node] = node_val
        yield node_val

    get_maximum_subtree_children(-1)

    # console("p", p)   
    # console("q", q)
    # console("other_roots", other_roots)

    # find roots
    roots = []
    stack = deque(g[-1])
    while stack:
        cur = stack.popleft()
        if p[cur] > 0 and (brr[cur-1] == -1 or p[brr[cur-1]] < 0):
            roots.append(cur)
        stack.extend(g[cur])

    # console("roots", roots)
    roots = sorted(roots, key=lambda x:p[x])
    roots = [root for root in roots if p[root] >= 0]
    # console("roots", roots)

    order = []

    stack = deque(roots)
    # console(stack)
    while stack:
        cur = stack.popleft()
        order.append(cur)
        stack.extend(q[cur])

    order = order[::-1]
    # console("order", order)

    visited = set(order)

    stack = deque(g[-1])
    # console("stack2", stack)
    while stack:
        cur = stack.popleft()
        if not cur in visited:
            order.append(cur)
        stack.extend(g[cur])

    # console("order", order)

    # simulate result
    score = 0
    for x in order:
        x = x-1
        score += arr[x]
        if brr[x] == -1:
            continue
        else:
            arr[brr[x]-1] += arr[x]
        # console(x+1, arr[x], arr)

    score2 = sum(p.values()) - p[-1]
    if score != score2:
        print(len(order), len(set(order)))
    print(score2)
    print(" ".join(str(x) for x in order))
    return None


def console(*args):  # the judge will not read these print statement
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return

# fast read all
# sys.stdin.readlines()

def main():
    # read line as a string
    # strr = input()

    # read line as an integer
    _ = int(input())
    
    # read one line and parse each word as a string
    # lst = input().split()

    # read one line and parse each word as an integer
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))

    # read matrix and parse as integers (after reading read nrows)
    # lst = list(map(int,input().split()))
    # nrows = lst[0]  # index containing information, please change
    # grid = []
    # for _ in range(nrows):
    #     grid.append(list(map(int,input().split())))

    solve(arr, brr)  # please change
    
    # Google - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Codeforces - no case number required
    # print(res)

main()