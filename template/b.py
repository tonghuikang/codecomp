from functools import lru_cache

def solve(arr,k):
    # print(k, arr)
    arr = arr.strip("0")
    if arr == "":
        return 0

    arr = [int(x) for x in list(arr)]
    brr = [1 for x in arr]  # for calculations

    summ = sum(arr)
    # print(sum(arr))

    crr = [sum(arr[i::k]) for i in range(k)]   # already ones
    drr = [summ - sum(arr[i::k]) for i in range(k)]   # should be zeroes
    err = [sum(brr[i::k]) for i in range(k)]   # should be ones 
    frr = [summ - sum(brr[i::k]) for i in range(k)]
    
    res = [e-c + d for c,d,e,f in zip(crr,drr,err,frr)]
    # print(crr)
    # print(drr)
    # print(err)
    # print(res)
    return min(res)


for _ in range(int(input())):
    _,k = list(map(int,input().split()))
    arr = input()
    print(solve(arr,k))
