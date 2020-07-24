# Specific algorithms

Please understand the concepts, e.g. optimal substructure.

https://judge.yosupo.jp/

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





### Maximum subarray

not contest tested yet

```python
import sys
def maxSubArraySum(arr): 
       
    max_so_far = -sys.maxint - 1
    max_ending_here = 0
       
    for a in arr: 
        max_ending_here = max_ending_here + a 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 
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
class Solution:
  def longestCommonSubsequence(self, A: str, B: str):
    n, m = len(A), len(B)
    dp = [[0] * (m) for i in range(n)]
    for i in range(n):
      for j in range(m):
        # value condition
        dp[i][j] = int(A[i] == B[j])
        if i>0 and j>0: 
          dp[i][j] += max(dp[i - 1][j - 1], 0)
        if i>0:
          dp[i][j] = max(dp[i][j], dp[i - 1][j])
        if j>0:
          dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[-1][-1]
```

The longest palindromic subsequence is the long common subsequence of the current and reversed string.

[Max Dot Product of Two Subsequences](https://leetcode.com/problems/max-dot-product-of-two-subsequences/) is similar as well.

You have a rectangular matrix, you start from outside the top left edge and you can jump to a box strictly left and strictly below of your box.



**Minimum Spanning Tree**

```python
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected, undirected and weighted graph 
  
from collections import defaultdict 
  
#Class to represent a graph 
class Graph: 
  
    def __init__(self, vertices): 
        self.V = vertices # number of vertices
        self.graph = [] # default dictionary to store graph 
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
    # The main function to construct MST using Kruskal's algorithm 
    def KruskalMST(self): 
  
        result = [] # This will store the resultant MST 
  
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 
  
        # Step 1: Sort all the edges in non-decreasing order of their weight. 
        # If we are not allowed to change the given graph, we can create a copy of graph 
        self.graph = sorted(self.graph, key=lambda item: item[2]) 
  
        parent = []
        rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V-1 : 
  
            # Step 2: Pick the smallest edge and increment the index for next iteration 
            u,v,w = self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent, v) 
  
            # If including this edge does't cause cycle, 
            # include it in result and increment the index of result for next edge 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 
  
        return result
  
# Driver code 
g = Graph(4) 
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4) 
  
g.KruskalMST()
```