import sys

from collections import defaultdict
import bisect

def solve(nums):
    nums = sorted(nums)
    mp = defaultdict(list)
    nonzeros = 0

    for i in range(len(nums)):
        mp[nums[i]].append(i)

        if nums[i] != 0:
            nonzeros += 1

    res = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            val = nums[i] * nums[j]
            if val in mp:
                idx = bisect.bisect_right(mp[val], j)
                res += len(mp[val])-idx
            
            if nums[i] == 0 and nums[j] == 0:
                res+= nonzeros
    return res

testCases = int(input())

for testCase in range(1, testCases + 1):
    n = int(input())
    b = list(map(int, input().split()))
    
    res = solve(b)
    print("Case #{}: {}".format(testCase, res))
        
