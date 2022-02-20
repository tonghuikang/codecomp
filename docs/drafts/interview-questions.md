# Standard problems

You do not have access to Google search during the interview, so all the best.

From https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-75-LeetCode-Questions-to-Save-Your-Time-OaM1orEU



### Arrays

- Two Sum - hashmap
- Three Sum - fix a number and Two Sum
- Four Sum - fix two numbers and Two Sum
- Maximum Subarray - prefix sum
- Maximum Product Subarray - prefix and suffix product
- Find Minimum in Rotated Sorted Array - binary search, add big M to elements larger than the first element
- Container with the most water - squeeze from left and right
- Longest Common Subarray - Slide one array across another. DP with LCS modified possible
- Merge Intervals - Prefix sum and check if point is positive
- Kth largest element - ???



### Dynamic Programming

- Cilmbing Stairs
- Coin Change
- Longest Increasing Subsequence (LIS) - DP containing the smallest possible number in the LIS at each position

```python
def longest_increasing_subsequence(nums):
    dp = [MAXINT] * (len(nums) + 1)
    for elem in nums:
        dp[bisect.bisect_left(dp, elem)] = elem  
    return dp.index(MAXINT)
```

- Longest Common Subsequence (LCS) - DP containing best score each index
- Word Break Problem - DFS and memomise the suffix
- Coin Change - DP of number of ways for each value, starting from each coin



### Graph

- Course Schedule - Topological Sort - iterate along courses with no dependencies
- Number of Islands - Count connected components



### Linked List

- Detect Cycle in a Linked List - Tortoise and Hare, do simple algebra



### Matrix

- Spiral matrix - Recursive solution



### String

- Valid Parentheses - stack, and check if empty at end
- Longest Palindromic Substring - Longest Common Substring with reverse
- Longest Substring Without Repeating Characters - Two pointers
- Longest Repeating Substring After Character Replacement - ???



### Tree

- Check If Rooted Trees Are Equal - encode subtree with parentheses
- Preorder Traversal (node, left, right)
- Inorder Traversal (left, node, right)
- Postorder Traversal (left, right, node)
- Kth ancestor of a Tree Node - Binary Lifting
- Implement Trie - Define class TrieNode with attribute children that is a defaultdict of TrieNode



### Heap

- Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
- Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
- Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/



### Standard problems

- Solve Sudoku - DFS the solutions



### Game theory

- Cat and Mouse
  - Each node is a state of the game (position of mouse, position of cat, whose turn)
  - Color each node as draw by default.
  - Color ending position
  - Propagate

