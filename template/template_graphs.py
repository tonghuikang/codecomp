#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

from template_recursive import dfs

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------

# to visualise graphs https://csacademy.com/app/graph_editor/

# ------------------------ basic graph operations ------------------------


def visit_accessible(map_from_node_to_nodes, start, visited=set()):
    # binarysearch.com/problems/Connected-Cities
    if not visited:
        visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        cur = stack.pop()
        for nex in map_from_node_to_nodes[cur]:
            if nex in visited:
                continue
            visited.add(nex)
            stack.append(nex)
    return visited


def count_connected_components_undirected(map_from_node_to_nodes, total_elements=0):
    # leetcode.com/problems/number-of-operations-to-make-network-connected
    visited = set()
    components = 0

    for node in map_from_node_to_nodes:
        if node in visited:
            continue
        visited = visit_accessible(map_from_node_to_nodes, start=node, visited=visited)
        components += 1
    if not total_elements:  # if all elements are already specified in the map
        return components

    return components + total_elements - len(map_from_node_to_nodes)


def find_strongly_connected_components(graph):
    # github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/scc.py
    # input - list of node to nodes?

    # Given a directed graph, this returns a list of lists containing 
    # the strongly connected components in topological order.

    # Note that this implementation can be also be used to check if a directed graph is a
    # DAG, and in that case it can be used to find the topological ordering of the nodes.
    SCC, S, P = [], [], []
    depth = [0] * len(graph)

    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]


def is_bipartite(list_of_node_to_nodes):
    # leetcode.com/problems/is-graph-bipartite/discuss/119514/
    n, colored = len(list_of_node_to_nodes), {}
    for i in range(n):
        if i not in colored and list_of_node_to_nodes[i]:
            colored[i] = 1
            queue = collections.deque([i])
            while queue:
                cur = queue.popleft()
                for nex in list_of_node_to_nodes[cur]:
                    if nex not in colored:
                        colored[nex] = -colored[cur]
                        queue.append(nex)
                    elif colored[nex] == colored[cur]:
                        return False
    # you can obtain the 2-coloring from the `colored` as well
    return True


# ------------------------ shortest path ------------------------


def shortest_path_constant_cost(map_from_node_to_nodes, source, target):
    # to be tested
    # no path is produced here
    d = map_from_node_to_nodes
    stack = deque([source])
    visited = {source: 0}
    while stack:
        cur = stack.popleft()
        for nex in d[cur]:
            if nex in visited:
                continue
            stack.append(nex)
            visited[nex] = visited[cur] + 1
            if nex == target:
                return visited[nex]
    return sys.maxsize


def dijkstra(list_of_indexes_and_costs, start):
    # shortest path with nonnegative edge costs
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    length = len(list_of_indexes_and_costs)
    visited = [False] * length
    weights = [MAXINT] * length
    path = [None] * length
    queue = []
    weights[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        g, u = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in list_of_indexes_and_costs[u]:
            if not visited[v]:
                f = g + w
                if f < weights[v]:
                    weights[v] = f
                    path[v] = u
                    heapq.heappush(queue, (f, v))
    return path, weights


def dijkstra_with_preprocessing(map_from_node_to_nodes_and_costs, source, target, idxs=set()):
    # this operation is costly, recommend to parse to list_of_indexes_and_costs directly
    # leetcode.com/problems/path-with-maximum-probability/
    # leetcode.com/problems/network-delay-time/
    d = map_from_node_to_nodes_and_costs

    if target not in d:  # destination may not have outgoing paths
        d[target] = []
    if source not in d:
        return MAXINT

    # assign indexes
    if idxs:
        idxs = {k: i for i, k in enumerate(idxs)}
    else:
        idxs = {k: i for i, k in enumerate(d.keys())}

    # populate list of indexes and costs
    list_of_indexes_and_costs = [[] for _ in range(len(idxs))]
    for e, vrr in d.items():
        for v, cost in vrr:
            list_of_indexes_and_costs[idxs[e]].append((idxs[v], cost))

    _, costs = dijkstra(list_of_indexes_and_costs, idxs[source])
    return costs[idxs[target]]


def floyd_warshall(n, edges, LARGE=10**18):
    # https://github.com/cheran-senthil/PyRival/blob/pyrival/graphs/floyd_warshall.py
    # not sure what pred is for
    dist = [[0 if i == j else LARGE for i in range(n)] for j in range(n)]
    pred = [[None] * n for _ in range(n)]

    for u, v, d in edges:
        dist[u][v] = d
        pred[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred


# ------------------------ flow algorithms ------------------------


def maximum_bipartite_matching(map_from_node_to_nodes):
    # maximum independent set = total vertexes — edges in maximum matching
    raise NotImplementedError


class Dinic:
    # codeforces.com/contest/1473/submission/104332748
    # max flow algorithm

    # codeforces.com/contest/1473/submission/111242916
    # for slightly faster and smaller memory usage
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def bfs(self, s, t):
        self.level = level = [None] * self.N
        deq = deque([s])
        level[s] = 0
        G = self.G
        while deq:
            v = deq.popleft()
            lv = level[v] + 1
            for w, cap, _ in G[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    deq.append(w)
        return level[t] is not None

    def dfs(self, v, t, f):
        if v == t:
            return f
        level = self.level
        for e in self.it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        INF = 10**9 + 7
        G = self.G
        while self.bfs(s, t):
            (*self.it,) = map(iter, self.G)
            f = INF
            while f:
                f = self.dfs(s, t, INF)
                flow += f
        return flow


# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))

# last = [-1 for i in range(101)]

# G = Dinic(n+2)

# res = 0
# for i in range(n):
#     if b[i] > 0:
#         res += b[i]
#         G.add_edge(i+1,n+1,b[i])
#     else:
#         G.add_edge(0,i+1,-b[i])

#     pre = last[a[i]]
#     if pre!=-1:
#         G.add_edge(pre+1,i+1,10**15)
#     for j in range(pre+1,i):
#         if a[i]%a[j]==0:
#             G.add_edge(j+1,i+1,10**15)

#     last[a[i]] = i

# print(res-G.flow(0,n+1))


def min_cost_flow(map_from_node_to_nodes_and_capcities, demands):
    # see above
    raise NotImplementedError


# ------------------------ methods using disjoint set ------------------------


class DisjointSet:
    # leetcode.com/problems/accounts-merge/
    def __init__(self, parent={}):
        if not parent:
            parent = {}
        self.parent = parent

    def find(self, item):
        if item not in self.parent:
            self.parent[item] = item
            return item
        elif self.parent[item] == item:
            return item
        else:
            res = self.find(self.parent[item])
            self.parent[item] = res
            return res

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        self.parent[root1] = root2


class DisjointSet:
    # github.com/not522/ac-library-python/blob/master/atcoder/dsu.py
    # faster implementation of DSU
    def __init__(self, n: int) -> None:
        self.parent_or_size = [-1] * n

    def union(self, a: int, b: int) -> int:
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return x

        if -self.parent_or_size[x] < -self.parent_or_size[y]:
            x, y = y, x

        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x

        return x

    def find(self, a: int) -> int:
        parent = self.parent_or_size[a]
        while parent >= 0:
            if self.parent_or_size[parent] < 0:
                return parent
            self.parent_or_size[a], a, parent = (
                self.parent_or_size[parent],
                self.parent_or_size[parent],
                self.parent_or_size[self.parent_or_size[parent]],
            )
        return a

    def size(self, a: int) -> int:
        return -self.parent_or_size[self.find(a)]
    
    def get_groups(self):
        groups = defaultdict(list)
        for i in range(len(self.parent_or_size)):
            # not sure if this changes anything
            self.find(i)

        for i in range(len(self.parent_or_size)):
            groups[self.find(i)].append(i)

        return groups.values()


def minimum_spanning_tree(edges, costs):
    # leetcode.com/problems/min-cost-to-connect-all-points
    # leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
    if len(edges) == len(costs) == 0:
        return 0
    ds = DisjointSet()
    total_tree_cost = 0
    costs, edges = zip(*sorted(zip(costs, edges)))  # sort based on costs
    for cost, (u, v) in zip(costs, edges):
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            total_tree_cost += cost
    return total_tree_cost


def topological_sort(map_from_node_to_nodes, all_nodes=set()):
    # leetcode.com/problems/course-schedule-ii/
    indegree_counter = defaultdict(int)
    for lst in map_from_node_to_nodes.values():
        for v in lst:
            indegree_counter[v] += 1

    if not all_nodes:  # assume all nodes are found in the map
        all_nodes = set(indegree_counter.keys()) | set(map_from_node_to_nodes)

    dq = deque([node for node in all_nodes if node not in indegree_counter])

    res = []
    while dq:
        cur = dq.popleft()
        res.append(cur)
        for nex in map_from_node_to_nodes[cur]:
            indegree_counter[nex] -= 1
            if indegree_counter[nex] == 0:
                dq.append(nex)
    return res if len(res) == len(all_nodes) else []


def detect_cycle(map_from_node_to_nodes):
    if not map_from_node_to_nodes:
        return False
    # leetcode.com/problems/course-schedule/
    return topological_sort(map_from_node_to_nodes) == []


def find_shortest_cycle(n: int, edges: list[list[int]]) -> int:
    # https://web.archive.org/web/20170829175217/http://webcourse.cs.technion.ac.il/234247/Winter2003-2004/ho/WCFiles/Girth.pdf
    # Time complexity: O(VE)

    g = defaultdict(set)
    for a, b in edges:
        g[a].add(b)
        g[b].add(a)

    inf = 10**18
    minres = inf

    for start in range(n):
        visited = set()
        queue = deque([start])
        parents = {start: None}
        depth = {start: 0}

        while queue:
            x = queue.popleft()
            visited.add(x)

            for y in g[x]:
                if y == parents[x]:
                    continue
                if y not in visited:
                    parents[y] = x
                    depth[y] = depth[x] + 1
                    queue.append(y)
                else:
                    minres = min(minres, depth[x] + depth[y] + 1)

    if minres == inf:
        return -1
    return minres


def longest_path_in_tree(list_of_node_to_nodes_and_costs):
    # https://leetcode.com/problems/minimum-height-trees
    # https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
    # assumes input is a tree
    n = len(list_of_node_to_nodes_and_costs)
    
    def dfs(start):   
        path = [None for _ in range(n)]
        weights = [None for _ in range(n)]
        weights[start] = 0

        stack = [start]
        visited = set([start])
        
        while stack:
            cur = stack.pop()
            for nex, cost in list_of_node_to_nodes_and_costs[cur]:
                if nex in visited:
                    continue
                visited.add(nex)
                weights[nex] = weights[cur] + cost
                path[nex] = cur
                stack.append(nex)
                
        return path, weights
    
    _, weights = dfs(0)
    start = weights.index(max(weights))

    path, weights = dfs(start)
    distance = max(weights)
    cur = weights.index(distance)
        
    max_dist_path = [cur]
    while cur != start:
        cur = path[cur]
        max_dist_path.append(cur)
    
    return max_dist_path, distance


def get_forest_sizes(map_from_node_to_nodes):  # UNTESTED
    # assumes that input is a tree
    # For each node, get the sizes of the forests if the tree is split on the node
    # uses the dfs template - see template_recursive.py

    n = len(map_from_node_to_nodes)
    subtree_sizes = {x: 1 for x in map_from_node_to_nodes}
    parents = {}

    def entry_operation(prev, cur, nex):
        # note that prev is `null_pointer` at the root node
        parents[nex] = cur

    def exit_operation(prev, cur):
        subtree_sizes[prev] += subtree_sizes[cur]

    start = next(iter(map_from_node_to_nodes))
    parents[start] = "NULL"
    dfs(start, map_from_node_to_nodes, entry_operation, exit_operation)

    node_to_forest_sizes = {}
    for cur in map_from_node_to_nodes:

        forest_sizes = []
        for nex in map_from_node_to_nodes[cur]:
            if nex != parents[cur]:
                forest_sizes.append(subtree_sizes[nex])

        parent_size = n - sum(forest_sizes) - 1
        if parent_size != 0:
            forest_sizes.append(parent_size)

        node_to_forest_sizes[cur] = forest_sizes

    return node_to_forest_sizes


def find_centroids(map_from_node_to_nodes):  # UNTESTED
    # Centroid of a tree is a node which if removed from the tree would split it into a 'forest',
    # such that any tree in the forest would have at most half the number of vertices in the original tree
    # the centroids is one or two points that

    # assumes that input is a tree
    node_to_forest_sizes = get_forest_sizes(map_from_node_to_nodes)

    n = len(map_from_node_to_nodes)

    centroid_candidates = []
    min_max_forest_size = n

    for cur, forest_sizes in node_to_forest_sizes.items():
        max_forest_size = max(forest_sizes)
        if max_forest_size == min_max_forest_size:
            centroid_candidates.append(cur)
        elif max_forest_size < min_max_forest_size:
            centroid_candidates = [cur]
            min_max_forest_size = max_forest_size

    return centroid_candidates


def extract_subgraph(map_from_node_to_nodes, source_point, break_point):
    # dfs starting from the source_point
    # break at the break point
    # return pruned graph
    pass


def find_bridges():
    # https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/
    # https://cp-algorithms.com/graph/bridge-searching.html
    # https://cp-algorithms.com/graph/bridge-searching-online.html
    return NotImplementedError


def find_articulation_points():
    # https://cp-algorithms.com/graph/cutpoints.html
    return NotImplementedError


# ------------------------ other methods ------------------------


def clique_cover(edges, N):
    # clique cover https://en.wikipedia.org/wiki/Clique_cover
    # https://atcoder.jp/contests/abc187/tasks/abc187_f
    # https://atcoder.jp/contests/abc187/submissions/19150883
    # the chromatic number is clique cover of the non-edges of the of the graph
    # https://codeforces.com/blog/entry/57496
    # https://codegolf.stackexchange.com/questions/37709/find-the-chromatic-number
    # to edit the following to follow the format, to understand what is going on also
    edges = set(tuple(edge) for edge in edges)
    ccs = [[1]]
    ret = 100

    def visit(pos):
        nonlocal ret
        # debug(pos, ccs, msg=":pos")
        if pos == N + 1:
            if len(ccs) < ret:
                ret = len(ccs)
                # debug(msg=":min")
            return
        if len(ccs) >= ret:
            # debug(msg=":early stop")
            return

        for cc in ccs:
            if all((v, pos) in edges for v in cc):
                # can join the cc
                cc.append(pos)
                visit(pos + 1)
                cc.pop()

        # create new cc
        # cid = len(ccs)
        ccs.append([pos])
        # vcc[pos - 1] = cid
        visit(pos + 1)
        ccs.pop()

    visit(2)
    return ret


def is_planar(graph):
    # a graph is planar iff there is no K5 or K3,3 subgraph
    # github.com/networkx/networkx/blob/main/networkx/algorithms/planarity.py
    # github.com/networkx/networkx/pull/3040
    # https://en.wikipedia.org/wiki/Planarity_testing
    # https://en.wikipedia.org/wiki/Left-right_planarity_test
    return NotImplementedError
