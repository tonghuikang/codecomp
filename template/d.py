#!/usr/bin/env python3
import sys
input = sys.stdin.readline  # to read input quickly

abc = "abcdefghijklmnopqrstuvwxyz"
abc_map = {c:i for i,c in enumerate(abc)}

if True:
    n,m = list(map(int,input().split()))
    mrr = [input().strip() for _ in range(n)]

    # your solution here
    mrr = [list(row) for row in mrr]

    rows = [[0 for _ in range(26)] for _ in range(n)]
    cols = [[0 for _ in range(26)] for _ in range(m)]

    rowset = set(range(n))
    colset = set(range(m))

    for i in range(n):
        for j in range(m):
            x = abc_map[mrr[i][j]]
            mrr[i][j] = x
            rows[i][x] += 1
            cols[j][x] += 1

    def check(counter):
        return sum(counter) == max(counter) >= 2

    flag = True
    while flag:
        flag = False
        rowset_to_remove = set()
        colset_to_remove = set()

        for i in rowset:
            c = rows[i]
            if check(c):
                flag = True
                rowset_to_remove.add(i)
        
        for j in colset:
            c = cols[j]
            if check(c):
                flag = True
                colset_to_remove.add(j)

        for i in rowset_to_remove:
            rowset.remove(i)

        for j in colset_to_remove:
            colset.remove(j)

        for i in rowset:
            for j in colset_to_remove:
                x = mrr[i][j]
                rows[i][x] -= 1

        for j in colset:
            for i in rowset_to_remove:
                x = mrr[i][j]
                cols[j][x] -= 1

    print(len(rowset) * len(colset))

