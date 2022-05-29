#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# for segment trees, see template_segment_trees.py

# ------------------------ standard imports ends here ------------------------

# ------------------------------ Binary Lifting ------------------------------


N = 2**20 + 2
root = 0
anc = [None for i in range(N)]  # anc[u][k] is (2**k)-th ancestor of u
anc[root] = [-1] * 20
anc[-1] = [-1] * 20

def buildJumps(u, parent):
    jumps = [0] * 20
    jumps[0] = parent
    for i in range(1, 20):
        jumps[i] = anc[jumps[i - 1]][i - 1]   # avoided writing into a matrix here
    anc[u] = jumps

def getLast(u, f):
    # Returns highest node on the path from u to root where f(node) is true.
    # Assumes f is monotonic and goes from true to false (from node to root)
    # If all false, returns u.
    for i in reversed(range(20)):
        if f(anc[u][i]):   # attempted to jump 2**i up, jumps if non-zero
            u = anc[u][i]
    return u


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
            for c,obj in zip(word[::-1], objects[:-1][::-1]):
                if not obj[c]:
                    del obj[c]
                else:
                    break

        # assert word not in self  # confirm that the number has been removed


# -------------------------- Fenwick Tree --------------------------


class FenwickTree:
    # also known as Binary Indexed Tree
    # binarysearch.com/problems/Virtual-Array
    # https://leetcode.com/problems/create-sorted-array-through-instructions
    # may need to be implemented again to reduce constant factor

    # ALL ELEMENTS ARE TO BE POSITIVE
    def __init__(self, bits=31):
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
    t = FenwickTree(bits = len(bin(max(perm))))
    for i,x in enumerate(perm):
        cnt = t.query(x)
        res += i-cnt
        t.update(x, 1)
    return res


# ----------------------- Self-balancing Trees -----------------------

# todo
# - Cartesian Tree