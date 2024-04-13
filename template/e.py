#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly

def solve_(n, arr):
    flag = True

    # nonzero = list(range(n))

    cnt = 2 * int(200_000 ** 0.5) + 20
    while cnt:
        cnt -= 1
        # flag = False

        # nexarr = []

        for i in range(n):
            cur = i
            nex = i+1
            if cur == n-1:
                nex = 0

            if arr[cur] == 0:
                continue
            if arr[nex] > 0:
                # flag = True
                arr[nex] = max(0, arr[nex] - arr[cur])

                # if arr[nex] > 0:
                #     nexarr.append(cur)
        
        # nonzero = nexarr

    for i in range(n):
        if arr[i] > 0 and arr[(i+1)%n] > 0:
            arr[(i+1)%n] = 0

    return [i for i,x in enumerate(arr) if x > 0]


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve_(n, arr)  # include input here

    # print length if applicable
    print(len(res))

    # parse result
    res = " ".join(str(x+1) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
