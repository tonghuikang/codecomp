#!/usr/bin/env python3
import sys, getpass
input = sys.stdin.readline  # to read input quickly


# ---------------------------- template ends here ----------------------------





# read line as an integer
k = int(input())

# read line as a string
# srr = input().strip()

# read one line and parse each word as a string
# lst = input().split()

# read one line and parse each word as an integer
# a,b,c = list(map(int,input().split()))
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))

# read multiple rows
# mrr = read_matrix(k)  # and return as a list of list of int
# arr = read_strings(k)  # and return as a list of str

mult = [a*b for a,b in zip(arr,brr)]
# consider all possible centres
# log(sum(mult))

# odd centres
max_addres = 0
for c in range(k):
    curres = 0
    left = c
    righ = c
    while True:
        left -= 1
        righ += 1
        if left < 0 or righ >= k:
            break
        old = mult[left] + mult[righ]
        new = arr[righ]*brr[left] + arr[left]*brr[righ]
        # log(left, righ)
        curres += new - old
        max_addres = max(max_addres, curres)
    
# log("x")
for c in range(k):
    curres = 0
    left = c+1
    righ = c
    while True:
        left -= 1
        righ += 1
        if left < 0 or righ >= k:
            break
        old = mult[left] + mult[righ]
        new = arr[righ]*brr[left] + arr[left]*brr[righ]
        # log(left, righ)
        curres += new - old
        max_addres = max(max_addres, curres)

print(sum(mult) + max_addres)
