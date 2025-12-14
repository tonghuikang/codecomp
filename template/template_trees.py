#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# for segment trees, see template_segment_trees.py

# ------------------------ standard imports ends here ------------------------


class RangeQuery:
    # range minimum query, range maximum query, rmq
    # also known as sparse table
    # https://codeforces.com/contest/1696/submission/161778620
    def __init__(self, data, func=min):
        # func has to satisfy func(x, x) = x
        # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/lca.py
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        # queries data[begin:end]
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])


class LowestCommonAncestor:
    # https://cp-algorithms.com/graph/lca_binary_lifting.html
    # https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/
    # https://leetcode.com/problems/grid-teleportation-traversal/
    def __init__(self, n: int, graph: list[list[int]], root=0):
        self.n = n
        self.graph = graph
        self.logn = math.ceil(math.log2(n))
        self.depth = [-1 if i != root else 0 for i in range(n)]
        self.parent = [[-1] * n for _ in range(self.logn)]
        # the immediate parent is self.parent[0][node]

        self.dfs(root)
        self.doubling()

    def dfs(self, v: int, p=-1):
        for e in self.graph[v]:
            if e == p:
                continue
            self.parent[0][e] = v
            self.depth[e] = self.depth[v] + 1
            self.dfs(e, v)

    def doubling(self):
        for i in range(self.logn - 1):
            for v in range(self.n):
                if self.parent[i][v] != -1:
                    self.parent[i + 1][v] = self.parent[i][self.parent[i][v]]

    def get(self, u: int, v: int):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for i in range(self.logn):
            if ((self.depth[v] - self.depth[u]) >> i) & 1:
                v = self.parent[i][v]
        if u == v:
            return u
        for i in range(self.logn - 1, -1, -1):
            if self.parent[i][u] != self.parent[i][v]:
                u, v = self.parent[i][u], self.parent[i][v]
        return self.parent[0][u]


# ----------------------------------- Trie -----------------------------------


class Trie:
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
    def __init__(self, *words):
        self.root = dict()
        for word in words:
            self.add(word)

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, dict())
        current_dict["_end_"] = True

    def __contains__(self, word):
        current_dict = self.root
        for letter in word:
            if letter not in current_dict:
                return False
            current_dict = current_dict[letter]
        return "_end_" in current_dict

    def delete(self, word, prune=False):
        current_dict = self.root
        nodes = [current_dict]
        objects = []
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
            objects.append(current_dict)

        del current_dict["_end_"]

        if prune:
            # https://leetcode.com/problems/maximum-genetic-difference-query/discuss/1344900/
            for c, obj in zip(word[::-1], objects[:-1][::-1]):
                if not obj[c]:
                    del obj[c]
                else:
                    break

        # assert word not in self  # confirm that the number has been removed


# -------------------------- Fenwick Tree --------------------------


class FenwickTreeSparse:
    # refer to template/template_sortedlist_c_tourist.py instead
    # also known as Binary Indexed Tree
    # binarysearch.com/problems/Virtual-Array
    # https://leetcode.com/problems/create-sorted-array-through-instructions
    # may need to be implemented again to reduce constant factor

    # ALL ELEMENTS ARE TO BE POSITIVE
    def __init__(self, bits=31):  # NOTE: THIS VALUE CAN TLE
        self.c = defaultdict(int)
        self.LARGE = 2**bits

    def update(self, x, increment):
        # future query(y) to increase for all y >= x
        x += 1  # to avoid infinite loop at x > 0
        while x <= self.LARGE:
            # increase by the greatest power of two that divides x
            self.c[x] += increment
            x += x & -x

    def query(self, x):
        x += 1  # to avoid infinite loop at x > 0
        res = 0
        while x > 0:
            # decrease by the greatest power of two that divides x
            res += self.c[x]
            x -= x & -x
        return res


def count_inversions(perm):
    # number of adjacent inversions needed to return to identity permutation
    # for each index, count how many numbers on its left that are larger
    # this is also a sample on how to use the class
    res = 0
    t = FenwickTreeSparse(bits=len(bin(max(perm))))
    for i, x in enumerate(perm):
        cnt = t.query(x)
        res += i - cnt
        t.update(x, 1)
    return res


# ----------------------- Self-balancing Trees -----------------------

# todo
# - Cartesian Tree
