# Specific algorithms

Please understand the concepts, e.g. optimal substructure.



Count number of permutations a number is divisible by 11. https://www.quora.com/log/revision/22296018

```python
import operator as op
from functools import reduce, lru_cache

def eval(lst):
    # lst = ins[5]
    L = sum(lst)
    M = (L+1)//2
    cnt = [0] + lst
    csum = [sum(cnt[i:]) for i in range(10)]

#     print(lst)
#     print(L)
#     print(M)
#     print(cnt)
#     print(csum)

    DP = [[[0 for _ in range(11)] for _ in range(M+1)] for _ in range(11)]
    DP[10][0][0]=1

    @lru_cache(maxsize=9999)
    def ncr(n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom

    C = ncr    

    for i in range(9,-1,-1):
      for j in range(0, M+1):
        for k in range(0, 10+1):
          for p in range(0,min(j,cnt[i])+1):
            j_=j-p
            k_=(k-i*(2*p-cnt[i]))%11
            if(i>0):
                DP[i][j][k]+=C(j,p)*C(csum[i]-j,cnt[i]-p)*DP[i+1][j_][k_]
            else:
                DP[i][j][k]+=C(j-1,p)*C(csum[i]-j,cnt[i]-p)*DP[i+1][j_][k_]
    
    if DP[0][M][0] > 0:
        return "YES"
    return "NO"
```





### Box pushing



```python
    def minPushBox(self, grid: List[List[str]]) -> int:
        
        free = set((i, j) 
                   for i, row in enumerate(grid) 
                   for j, cell in enumerate(row) 
                   if grid[i][j] != '#')

        target = next((i, j) 
                      for i, row in enumerate(grid) 
                      for j, cell in enumerate(row) 
                      if grid[i][j] == 'T')

        boxi, boxj = next((i, j) 
                          for i, row in enumerate(grid) 
                          for j, cell in enumerate(row) 
                          if grid[i][j] == 'B')

        si, sj = next((i, j) 
                      for i, row in enumerate(grid) 
                      for j, cell in enumerate(row) 
                      if grid[i][j] == 'S')

        visited = set()
        heap = [(0, si, sj, boxi, boxj)]

        while heap:
            moves, si, sj, boxi, boxj = heapq.heappop(heap)
            
            if (boxi, boxj) == target:
                return moves
            
            if (si, sj, boxi, boxj) in visited:
                continue
            
            visited.add((si, sj, boxi, boxj))
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = si + dx, dy + sj
                if ((ni, nj) == (boxi, boxj) 
                    and (boxi + dx, boxj + dy) in free 
                    and (ni, nj, boxi + dx, boxj + dy) not in visited):
                    heapq.heappush(heap, 
                                   (moves + 1, ni, nj, boxi + dx, boxj + dy))

                elif ((ni, nj) in free 
                      and (ni, nj, boxi, boxj) not in visited):
                    heapq.heappush(heap, 
                                   (moves, ni, nj, boxi, boxj))
        return -1
```



### Max sliding window

```python
class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        bigger = deque()
        for i, n in enumerate(nums):
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] <= n:
                bigger.pop()

            # add in
            bigger += [i]

            # make sure the leftmost one is in-bound
            if i - bigger[0] >= k:
                bigger.popleft()

            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[bigger[0]])
                
            print(bigger)
        return res        
```



Sliding window

- 1. [Count Number of Nice Subarrays](https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/419378/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1))
- 1. [Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/discuss/408978/javacpython-sliding-window/367697)
- 1. [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/javacpython-sliding-window/379427?page=3)
- 1. [Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/discuss/186683/)
- 1. [Subarrays with K Different Integers](https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/234482/JavaC%2B%2BPython-Sliding-Window-atMost(K)-atMost(K-1))
- 1. [Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/discuss/170740/Sliding-Window-for-K-Elements)
- 1. [Shortest Subarray with Sum at Least K](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/143726/C%2B%2BJavaPython-O(N)-Using-Deque)
- 1. [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/discuss/433123)



## Other standard problems

**Longest Common Subsequence**

```python
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        L = [[0 for _ in range(len(text2) + 1)] 
             for _ in range(len(text1) + 1)]
        
        for i in range(len(text1) + 1):
            for j in range(len(text2) + 1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    L[i][j] = L[i-1][j-1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        
        return L[-1][-1] 
```

The longest palindromic subsequence is the long common subsequence of the current and reversed string.