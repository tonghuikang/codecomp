# Leetcode Python Reference

[TOC]

Please study or include

- factorisation algorithm, and divisor counting
- knapsack of all variants
- the constraint programming solver code
- binary search implementation



## Common Code snippets

These are some code snippets I freqently use in Leetcode, in descending order. I place them here so that I do not need to use the search engine everytime I want it.

**Sorting a 2D list based on a certain index**. <br>
https://stackoverflow.com/questions/18563680/ <br>

```python
lst = sorted(lst,key=lambda e:e[1])
```

**Tranpose an array**

```python
zip(*theArray)
```

**Flatten a list of list**

```python
sum(arr, [])
```

**String range**
```python
def srange(a, b):
    yield from (chr(i) for i in range(ord(a), ord(b)+1))
```

**Making a freqency dictionary.** <br>
https://stackoverflow.com/questions/722697/ <br>

```python
from collections import defaultdict
fq = defaultdict(int)
for w in words:
    fq[w] += 1
```

```python
from collections import Counter
fq = Counter(lst)
```

**Python deque**

If you want a list that can be popped efficiently from either side.

```python
from collections import deque
```

Deleting the first element is quite fast as well.

```python
lst = range(10000)
del lst[0]
```

**Python heapq**

https://www.cs.usfca.edu/~galles/visualization/Heap.html

The interesting property of a heap is that its smallest element is always the root, heap[0].

```python
import heapq
heapq.heapify(lst)
heapq.heappush(heap, item)
heapq.heappop(heap)
```

- Transforming an array into a heap takes linear time $n$.
- Adding a element to the array takes $log(n)$ time. 
- Removing the smallest element from the array takes $log(n)$ time.

**Search an array efficiently in Python**

Does binary search for you.

https://docs.python.org/3/library/bisect.html

**List comprehensive with if and else**

```python
lst = [(i - 12*((i//12)-1)) if i>25 else i for i in lst]
```

**Using maxint because you are cool**

```python
import sys
MAX = sys.maxint
```

**Reduce excess whitespace**

Replace multiple whitespace with one whitespace.

```python
' '.join(mystring.split())
```

**Knapsack**

There are 0–1 knapsack, bounded knapsack, and unbounded knapsack. These are actually linear/integer/mixed programming problems. 

**Binary** Knapsack problem. For every item you may or may not take, and you need to fulfil the max limit.

```python
from functools import lru_cache

def knapsack(items, maxweight):
    # items is an array of (value, weight)
    @lru_cache(maxsize=None)
    def bestvalue(i, j):
        # Return the value of the most valuable 
        # subsequence of the first i elements in 
        # items whose weights sum to no more than j.
        if j < 0:
            return float('-inf')
        if i == 0:
            return 0
        value, weight, idx = items[i - 1]
        return max(bestvalue(i - 1, j), bestvalue(i - 1, j - weight) + value)

    j = maxweight
    result = []
    for i in reversed(range(len(items))):
        if bestvalue(i + 1, j) != bestvalue(i, j):
            result.append(items[i])
            j -= items[i][1]
    result.reverse()
    return bestvalue(len(items), maxweight), result

arr = [(a,b,c) for a,b,c in zip([16,22,12,8,11,19],
                                [5,7,4,3,4,6],
                                range(6))]
knapsack(arr, 15)
```

**Integer** Knapsack problem
https://rosettacode.org/wiki/Knapsack_problem/Bounded#Python

You no longer build by number of items selected, you iterate from the first possible item?

**Mixed linear programming**

This one you need to use a library.

**Integer factorisation (brute force)**

Just in case you need it.

```python
def factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors
```
## Binary Tree

One question is on binary trees, or uses binary trees. Some training is necessary to understand how to use them. Binary trees are constructed from an array and can be deconstructed and be represented by an array.

This is leetcode's definition of a binary tree.
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
```

This is a basic way to iterate a binary tree.
```
        def helper(node):
            if node == None:
                return None
            arr1.append(node.val)
            helper(node.left)
            helper(node.right)

        arr1 = []
        helper(root2)
```



## Graphs

There are a few types of graphs
- depending whether it is directed or undirected
- whether the nodes are weighted
- whether the edges are weighted

Official essay on Python graphs - https://www.python.org/doc/essays/graphs/

(Why didn't Python already have standard Graph object that implement common algorithms? Trying to make one here).

A tree is a directed graph with all (except the root node) with an indegree.

A **trie** is a tree-like data structure whose nodes store the letters of an alphabet. 



**Creating a graph from a grid**


```
        g = defaultdict(list)
        row_length = len(grid[0])

        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                yy = []
                if j != 0:
                    yy.append(j-1)
                if j != len(grid[0]) - 1:
                    yy.append(j+1)
    
                xx = []
                if i != 0:
                    xx.append(i-1)
                if i != len(grid) - 1:
                    xx.append(i+1)
    
                for x in xx:
                    y = j
                    if grid[i][j] != 0 and grid[x][y] != 0:
                        g[i*row_length + j].append(x*row_length + y)
                for y in yy:
                    x = i
                    if grid[i][j] != 0 and grid[x][y] != 0:
                        g[i*row_length + j].append(x*row_length + y)

```



**Creating a unweighted <u>directed</u> graph**<br>

- Using Topological Sort

```python
from collections import defaultdict

class UnweightedDirectedGraph: 
    def __init__(self,vertices): 
        # dictionary containing adjacency List 
        self.graph = defaultdict(list) 
        # number of vertices
        self.V = vertices  
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    # The function to do Topological Sort. 
    # It uses recursive topoSortUtil().
    def topoSort(self): 

        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack = []

        # Call the recursive helper function 
        for i in range(self.V):
            if visited[i] == False:
                res = self.topoSortUtil(i,i,visited,stack)
                
                # if cycle is detected
                if res == -1:
                    return -1

        # return a sorted array
        return stack 
        
    def topoSortUtil(self,v,start,visited,stack): 
  
        # Mark the current node as visited
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]: 

            # return to the starting point, graph is cyclic
            # no topo sort is possible
            if i == start:
                return -1

            if visited[i] == False: 
                # apply to nodes in the tree
                res = self.topoSortUtil(i,start,visited,stack)

                # propogate the result out
                if res == -1:
                    return -1
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v)
```

Usage of the Graph object.

```python
g = UnweightedDirectedGraph(6) 
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0)
g.topoSort() # for example
```

**Creating an <u>weighted</u> <u>undirected</u> graph**<br>

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/

Initialising with adjacency matrix.

```python
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
```

Usage of the Graph object.
```python
g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

g.additionalFunction()
```

**Obtain connected components from undirected graph**

```python
# Python program to print connected  
# components in an undirected graph 
class Graph: 

    # init function to declare class variables 
    def __init__(self,V): 
        self.V = V 
        self.adj = [[] for i in range(V)] 

    def DFSUtil(self, temp, v, visited): 

        # Mark the current vertex as visited 
        visited[v] = True

        # Store the vertex to list 
        temp.append(v) 

        # Repeat for all vertices adjacent 
        # to this vertex v 
        for i in self.adj[v]: 
            if visited[i] == False: 

                # Update the list 
                temp = self.DFSUtil(temp, i, visited) 
        return temp 

    # method to add an undirected edge 
    def addEdge(self, v, w): 
        self.adj[v].append(w) 
        self.adj[w].append(v) 

    # Method to retrieve connected components 
    # in an undirected graph 
    def connectedComponents(self): 
        visited = [] 
        cc = [] 
        for i in range(self.V): 
            visited.append(False) 
        for v in range(self.V): 
            if visited[v] == False: 
                temp = [] 
                cc.append(self.DFSUtil(temp, v, visited)) 
        return cc 
```

Obtain connected components without building a graph

```python
    synonyms = [["happy","joy"],
                ["sad","sorrow"],
                ["joy","cheerful"]],
    d = defaultdict(list)
    index = 0
    d_rev = {}
    for syn in synonyms:
        if not syn[0] in d_rev and not syn[1] in d_rev:
            index += 1
            d[index].append(syn[0])
            d[index].append(syn[1])
            d_rev[syn[0]] = index
            d_rev[syn[1]] = index
        elif syn[0] in d_rev:
            d[d_rev[syn[0]]].append(syn[1])
            d_rev[syn[1]] = d_rev[syn[0]]
        elif syn[1] in d_rev:
            d[d_rev[syn[1]]].append(syn[0])
            d_rev[syn[0]] = d_rev[syn[1]]
        else:
            pass
```


**Djistrka algorithm**

```python
nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F' :5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}}

unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = 'B'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)
```




## Other standard problems

**Longest Common Subsequence**

```python
        def lcs(X, Y, m, n ): 
    
            L = [[0]*(n+1) for _ in range(m+1)] 
    
            # Following steps build 
                # L[m+1][n+1] in bottom up 
                # fashion. Note that L[i][j] 
                # contains length of 
            # LCS of X[0..i-1] and Y[0..j-1]  
            for i in range(m+1): 
                for j in range(n+1): 
                    if not i or not j: 
                        L[i][j] = 0
                    elif X[i - 1] == Y[j - 1]: 
                        L[i][j] = L[i - 1][j - 1] + 1
                    else: 
                        L[i][j] = max(L[i - 1][j], L[i][j - 1]) 
    
            # L[m][n] contains length 
                # of LCS for X and Y 
            return L[m][n] 
```

The longest palindromic subsequence is the long common subsequence of the current and reversed string.

## Tricks

You can define a function within a function. Defining function outside 
You can define a function outside, but sometimes the function is inside an object, then you need to use the `self` which complicate matters.


## Complexity tricks

Say you want to determine whether an array contain something, for many times. Convert the array into a hashmap (i.e. dictionary) for fast calling.

Binary search insert is faster because there is no need to read the whole (sorted) array. Use `bisort` for this.

`del lst[0]` is constant time, but `lst = lst[1:]` requires iterating through the full array. Use `heapq` if necessary.


