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

\- Detect Cycle in a Linked List - Tortoise and Hare, do simple algebra



### Matrix

- Spiral matrix - Recursive solution



### String

- Valid Parentheses - stack, and check if empty at end
- Longest Palindromic Substring 

\- Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
\- Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/
\- Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
\- Valid Anagram - https://leetcode.com/problems/valid-anagram/
\- Group Anagrams - https://leetcode.com/problems/group-anagrams/
\- Valid Parentheses - https://leetcode.com/problems/valid-parentheses/
\- Valid Palindrome - https://leetcode.com/problems/valid-palindrome/
\- Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
\- Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/
\- Encode and Decode Strings (Leetcode Premium) - https://leetcode.com/problems/encode-and-decode-strings/

\---

Tree

\- Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/
\- Same Tree - https://leetcode.com/problems/same-tree/
\- Invert/Flip Binary Tree - https://leetcode.com/problems/invert-binary-tree/
\- Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/
\- Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/
\- Serialize and Deserialize Binary Tree - https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
\- Subtree of Another Tree - https://leetcode.com/problems/subtree-of-another-tree/
\- Construct Binary Tree from Preorder and Inorder Traversal - https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
\- Validate Binary Search Tree - https://leetcode.com/problems/validate-binary-search-tree/
\- Kth Smallest Element in a BST - https://leetcode.com/problems/kth-smallest-element-in-a-bst/
\- Lowest Common Ancestor of BST - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
\- Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/
\- Add and Search Word - https://leetcode.com/problems/add-and-search-word-data-structure-design/
\- Word Search II - https://leetcode.com/problems/word-search-ii/

\---

Heap

\- Merge K Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/
\- Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/
\- Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

You're welcome!








### Comments

- Edge cases (zeroes, boundaries, identity case)
- Conditions to simplify complexity (e.g. Four Sum but numbers are limited)

