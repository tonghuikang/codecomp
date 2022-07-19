#!/usr/bin/env python3
import sys
import heapq
input = sys.stdin.readline  # to read input quickly

# ---------------------------- template ends here ----------------------------
# import time

# upper_limit = time.time() + 3.9

def ceiling_division(numer, denom):
    return -((-numer)//denom)

mask = 2**18 - 1
m0 = mask
m1 = mask << 18
m2 = mask << 36

# print(bin(m2))


def ungroup(x):
    return (x&m2) >> 36, (x&m1) >> 18, (x&m0) 

def group(a,b,c):
    val = (a << 36) ^ (b << 18) ^ c
    # assert ungroup(val) == (a,b,c)
    return val

for case_num in range(int(input())):
    n,k = list(map(int,input().split()))

    n_cooldown = 100*n
    cnt = n_cooldown

    # your solution here

    arr = [group((x//k),k,x) for x in map(int,input().split())]
    # arr.sort()

    minn = ungroup(arr[0])[0]
    maxx = ungroup(arr[-1])[0]
    minres = maxx - minn

    if minres == 0:
        print(0)
        continue

    maxx = max(1, maxx)

    # maxx = -minarr
    # jump = max(1, min(int(maxarr // minarr) - 1, int(maxarr // k)))
    # jump = 1
    # log(jump)

    while ungroup(arr[0])[1] > 1 and cnt > 0:
        nx,i,x = ungroup(heapq.heappop(arr))

        i = max(1, min(ceiling_division(x, maxx), x // (nx+1)))
        nx = (x//i)
        heapq.heappush(arr, group(nx,i,x))

        # log((nx,i,x))

        maxx = max(maxx, nx)
        minn = ungroup(arr[0])[0]
        # if maxx - minn < minres:
        #     log((nx,i,x), maxx - minn)
        cnt -= 1
        if maxx - minn < minres:
            minres = maxx - minn
            cnt = n_cooldown
        if minres == 0:
            break

    print(minres)

# LARGE = 3000
# res = solve([1] + [LARGE]*(LARGE-1), LARGE, LARGE)
# print("ok", LARGE, res)

# LARGE = 10**5
# res = solve([1] + [LARGE]*(LARGE-1), LARGE, LARGE)
# print("ok", LARGE, res)

# LARGE = 10**5
# res = solve([LARGE - 100] + [LARGE]*(LARGE-1), LARGE, LARGE)
# print("ok", LARGE, res)

# LARGE = 10**5
# arr = list(range(LARGE - 10000, LARGE))
# res = solve(arr, len(arr), LARGE)
# print("ok", LARGE, res)

# for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified

    # read line as an integer
    # k = int(input())

    # read line as a string
    # srr = input().strip()

    # read one line and parse each word as a string
    # arr = input().split()

    # nsum = 0

    # read one line and parse each word as an integer
    # arr = minus_one(arr)

    # nsum += n

    # read multiple rows
    # arr = read_strings(k)  # and return as a list of str
    # mrr = read_matrix(k)  # and return as a list of list of int
    # mrr = minus_one_matrix(mrr)

    # res = solve(arr, n, k)  # include input here

    # print length if applicable
    # print(len(res))

    # parse result
    # res = " ".join(str(x) for x in res)
    # res = "\n".join(str(x) for x in res)
    # res = "\n".join(" ".join(str(x) for x in row) for row in res)

    # print result
    # print("Case #{}: {}".format(case_num+1, res))   # Google and Facebook - case number required

