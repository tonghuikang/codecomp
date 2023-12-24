#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly


# ---------------------------- template ends here ----------------------------


def solve(n,k,d,arr,vrr):
    # your solution here

    # grow once and reset, repeat
    maxres = d // 2

    # for each element of position i in arr
    # how many days is needed to grow to v

    # reset and grow once, repeat
    res = 0
    for i,x in enumerate(arr, start=1):
        if i == x:
            res += 1
    res += (d - 1) // 2
    maxres = max(maxres, res)

    # grow multiple, reset, and grow once and reset
    for q,b in enumerate(vrr, start=1):
        res = 0
        for i in range(n):
            if i < b:
                arr[i] += 1
            if arr[i] == i+1:
                res += 1
        res += (d - q - 1) // 2
        maxres = max(maxres, res)

    return maxres


# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    n,k,d = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    vrr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(n,k,d,arr,vrr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
