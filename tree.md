# Trees

[TOC]



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

This is a basic way to iterate a binary tree. Note that `node.left` and `node.right` can be called before or after.

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

You can define a function within a function.



## Trie

Trie is a prefix tree.

https://leetcode.com/problems/implement-trie-prefix-tree/discuss/58834/AC-Python-Solution

I have yet to fully understand this implementation, so I will check back later.

You are not supposed to store every word and every prefix in memory, as some solutions on Leetcode suggest.


```python
class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True
```



`<defaultdict>.get(<key>)` is different from `<defaultdict>[<key>]`. The former returns `None` if the key does not exist, the latter returns the template.



## AVL Tree

Self-balancing tree. Please refer to https://github.com/tonghuikang/binary-tree for a Python 2 implementation.



## Interval Tree

TBC