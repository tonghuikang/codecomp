#!/usr/bin/env python3
import sys

input = sys.stdin.readline  # to read input quickly

# ---------------------------- template ends here ----------------------------


def solve(srr):
    # your solution here

    n = len(srr)

    # brute force, leap over the question marks

    arr = [0 for _ in range(n)]
    jump = [0 for _ in range(n)]
    curjump = 1
    non_question_idx = n
    for i,x in list(enumerate(srr))[::-1]:
        arr[i] = non_question_idx
        jump[i] = curjump
        if x != "?":
            non_question_idx = i
            curjump = 1
        else:
            curjump += 1

    # log(arr)
    # log(jump)
    maxres = 0

    for i in range(n):
        for length in range(1, (n - i) // 2 + 1):
            j = i + length
            # log(i, j)

            x = i
            y = j

            while x < i+length and y < j+length:
                if srr[x] != srr[y] and srr[x] != "?" and srr[y] != "?":
                    break
                maxjump = max(jump[x], jump[y])
                x += maxjump
                y += maxjump
                
            if x >= i+length and y >= j+length:
                maxres = max(maxres, length)

    return maxres * 2


solve("A?"*2500)

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
for case_num in range(int(input())):
    # read line as an integer
    # n = int(input())
    # k = int(input())

    # read line as a string
    srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # read one line and parse each word as an integer
    # a,b,c = list(map(int,input().split()))
    # arr = list(map(int,input().split()))
    # arr = minus_one(arr)

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    res = solve(srr)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

    print(res)
