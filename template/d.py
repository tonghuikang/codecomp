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

base = 0
for a,b in zip(arr,brr):
    base += a*b
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
        # log(left, righ)
        curres += (arr[left]-arr[righ])*(brr[righ]-brr[left])
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
        curres += (arr[left]-arr[righ])*(brr[righ]-brr[left])
        max_addres = max(max_addres, curres)

print(base + max_addres)
