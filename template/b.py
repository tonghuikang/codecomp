from functools import lru_cache

@lru_cache(maxsize=None)
def find_factors(k):
    factors = []
    for i in range(1, int(k**0.5)+1):
        if k%i == 0:
            factors.append(i)
            factors.append(k//i)
    # print(k, factors)
    return factors

def solve(lst):
    # print(len(lst))

    res = [1 for _ in lst]
    for i,_ in enumerate(lst, start=1):
        for factor in find_factors(i):
            if lst[factor-1] < lst[i-1]:
                res[i-1] = max(1 + res[factor-1], res[i-1])
    
    # print(res)
    return max(res)




for _ in range(int(input())):
    _ = input()
    lst = list(map(int,input().split()))
    print(solve(lst))
