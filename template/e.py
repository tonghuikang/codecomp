#!/usr/bin/env python3
import sys
import heapq
input = sys.stdin.readline  # to read input quickly

from sortedcontainers import SortedList

def read_matrix(rows):
    return [list(map(int,input().split())) for _ in range(rows)]

def minus_one_matrix(mrr):
    return [[x-1 for x in row] for row in mrr]


for case_num in range(int(input())):

    n,m,k = list(map(int,input().split()))
    arr = list(map(int,input().split()))

    mrr = read_matrix(m)  # and return as a list of list of int
    mrr = minus_one_matrix(mrr)

    g = [set() for _ in range(n)]
    f = [set() for _ in range(n)]
    for a,b in mrr:
        g[a].add(b)
        f[b].add(a)

    sl = SortedList()
    queue = []
    start = 0

    droppings = []
    for i in range(n):
        if len(f[i]) == 0:
            queue.append((arr[i] + k, i))
            droppings.append((arr[i], i))

    droppings.sort(reverse=True)
    heapq.heapify(queue)

    starts = {}

    while queue:
        hour, cur = heapq.heappop(queue)
        starts[cur] = hour
        sl.add(hour)
        # log(hour, cur)
        for nex in g[cur]:
            f[nex].remove(cur)
            if len(f[nex]) == 0:
                if arr[nex] >= arr[cur]:
                    heapq.heappush(queue, ((hour // k) * k + arr[nex], nex))
                else:
                    heapq.heappush(queue, ((hour // k) * k + arr[nex] + k, nex))

    minres = sl[-1] - sl[0]
    # log(starts)

    # log(minres)

    f2 = [set() for _ in range(n)]
    for a,b in mrr:
        if starts[a] + k > starts[b]:
            f2[b].add(a)

    for _, dropper in droppings:
        sl.remove(starts[dropper])
        starts[dropper] -= k
        sl.add(starts[dropper])

        stack = [dropper]
        while stack:
            cur = stack.pop()
            for nex in g[cur]:
                if cur in f2[nex]:
                    if starts[nex] >= starts[cur] + k:
                        f2[nex].remove(cur)
                        if len(f2[nex]) == 0:
                            sl.remove(starts[nex])
                            starts[nex] -= k
                            sl.add(starts[nex])
                            stack.append(nex)
        # log(dropper, starts)
        res = sl[-1] - sl[0]
        minres = min(minres, res)
    
    print(minres)

