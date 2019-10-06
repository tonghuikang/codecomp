# Leetcode Python Reference


## Overview of this reference

**What this document contains** (to be updated)
- a reference to terminologies used in leetcode
- code snippets
- problems and their named solutions and implementation

**What this is not**

This does not teach you Python. Neither does this teach or algorithms. There is no step-by-step guide here.

This does not help you with anything other than helping people like me perform better at leetcode. For the full technical interview process please do refer to Yangshun's [tech interview handbook](https://yangshun.github.io/tech-interview-handbook), which I think it covers all aspects of the technical interview.


## Foreword

Spending one or two one-and-half hours every week on solving programming problems is pretty fun. I can see myself playing leetcode for a long time.

There are code snippets and references that would have helped me to become more efficient at coding. Here I am sharing with you what I have done for myself.

Moreover, many big companies have a coding interview at various stages of hiring. If entering these companies is your objective it is recommended that you are good at solving problems.

Of course, this is not enough to get hired. In the interview you need to clarify the problem, explain your approach and then justify the computational complexity, without being affected by the interview setting.

We also have to keep in mind the more important prerequsites of a good hire 
- good communication skills
- good discipline at work 
- ability to learn quickly

Why is Leetcode better? It offers weekly challenges which I am keen to participate. Moreover, it handles the input/output for you so that you can focus on the code that matters. (On the other hand, for CodeForces or Google CodeJam, you are required to parse the text input, which can be time consuming and error prone.)

This guide is will be an overview of concepts for people who have never taken a course on algorithms (like me). 

I use Python because I am more familiar with it.

All leetcode problems should be solvable with Python as well, because the question is very constrained. However, in coding competitions (like one you need to deploy an API that solves incoming challenges), the speed at which Python creates objects can be too slow.


**On problem solving**

This is this process to follow
- Understand the question
- Formula solution strategy
- Implement solution strategy
- Deliver solution

There are some insights to understanding this ideal process.
- Each step depends on the previous steps.
  - You cannot implement the solution without formulating a strategy. 
  - You cannot devise a strategy without understanding the question.
  - It may be possible that you understand the question wrong, and wasted time on the rest of the steps.
- Having a strategy does not mean that you have the ability to implement it.


## Leetcode setup

A starter code on Leetcode looks like this

```python
class Solution:
    def functionName(self, s: str) -> str:
        return s
```

If you are to run the code on your computer, this is how you check the result.

```
s = Solution()
print(s.functionName("test_string"))
```

[TODO: Consider the use of PySnooper here]

Here we consider the advantages and disadvantages of testing on your computer (for example writing on VSCode with a debugger)

Writing on Leetcode|Writing on local computer 
-----------------------------|--------------------------------------
No need to copy and paste anything.|**Require copying of starter code and test cases**, which might have error.
Debugging requires print statements.|**Dubugging tools** is available with your IDE
**Waiting time for the code to run**.|No waiting time.
A **cooldown** applies between running code.|No cooldown or limits.
**Submission** is easy, and there is a greater confidence that it works.|Requires copying to leetcode for submission. Copying might cause error again.
Shows **expected output** (not during competitions)|Does not show expected output.
Require manual work to **swtich between test cases**.|Test cases (and its results) can be saved and tested all at once.

In summary, writing on Leetcode is great if you are confident that your code will work in one sitting - this especially applies to the easy question. However, if you code involve extensive debugging, perhaps it might be better to bring your code offline.

## Terminologies

Difference between substring and subsequence

Lexicographic (not alphabetical) order - is ab > aaa > aa? yes (cite leetcode questions)

## Common Code snippets

These are some code snippets I freqently use in Leetcode, in descending order. I place them here so that I do not need to use the search engine everytime I want it.

**Sorting a 2D list based on a certain index**. <br>
https://stackoverflow.com/questions/18563680/ <br>

```python
lst = sorted(lst,key=lambda e:e[1])
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
```
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

```
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



## Tricks

You can define a function within a function. Defining function outside 
You can define a function outside, but sometimes the function is inside an object, then you need to use the `self` which complicate matters.


## Complexity tricks

Say you want to determine whether an array contain something, for many times. Convert the array into a hashmap (i.e. dictionary) for fast calling.

Binary search insert is faster because there is no need to read the whole (sorted) array. Use `bisort` for this.

`del lst[0]` is constant time, but `lst = lst[1:]` requires iterating through the full array. Use `heapq` if necessary.





