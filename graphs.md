# Graphs

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

