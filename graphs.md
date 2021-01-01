# Graphs

There are a few types of graphs

- depending whether it is directed or undirected
- whether the nodes are weighted
- whether the edges are weighted

Official essay on Python graphs - https://www.python.org/doc/essays/graphs/

A tree is a directed graph with all (except the root node) with an indegree. (Refer to tree.md)



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



**Disjoint Set Union**

```python
class DisjointSet:
    def __init__(self, vertices, parent):
        self.vertices = vertices
        self.parent = parent

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2
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

Contest tested - PyPy3 600k nodes 2 seconds

```python
import heapq as hq
import math

def dijkstra(G, s):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [None]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        visited[u] = True
        for v, w in G[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    hq.heappush(queue, (f, v))
    return path, weights


# d is a map from e to [(v1,cost), (v2,cost), ...]
# node indexes can be of any data type

# define your source and target
source = "source"
target = "target"

# processing edge matrix
idxs = {k:i for i,k in enumerate(d.keys())}
G = [[] for _ in range(len(idxs))]
for e,vrr in d.items():
    for v,cost in vrr:
        G[idxs[e]].append((idxs[v],cost))

_,costs = dijkstra(G, idxs[source])
res = costs[idxs[target]]
```


```python
# test code for dijkstra()
G = [[(1, 6), (3, 7)],
     [(2, 5), (3, 8), (4, -4)],
     [(1, -2), (4, 7)],
     [(2, -3), (4, 9)],
     [(0, 2)]]

print(dijkstra(G, 0))
```



dijkstra with stop limit

```python
        def dijkstra(G, s):
            n = len(G)
            visited = [[False for _ in range(n+1)] for _ in range(n)]
            weights = [[math.inf for _ in range(n+1)] for _ in range(n)]
            path = [[None for _ in range(n+1)] for _ in range(n)]
            queue = []
            weights[s][0] = 0
            hq.heappush(queue, (0, s, 0))
            while len(queue) > 0:
                g, u, p = hq.heappop(queue)
                
                if p > K:
                    continue
                    
                visited[u][p+1] = True
                for v, w in G[u]:
                    if not visited[v][p+1]:
                        f = g + w
                        if f < weights[v][p+1]:
                            weights[v][p+1] = f
                            path[v][p+1] = u
                            hq.heappush(queue, (f, v, p+1))
            return path, weights        
```

