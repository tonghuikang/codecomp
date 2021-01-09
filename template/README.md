# Competitive Programming Template

This is the template I use for competitive programming.

I mainly compete in Codeforces and AtCoder.

(I also participate in LeetCode Weekly Contests, but I use their online IDE. I recommend starting out from there.)


# How to use

Copy the test case to `a0`. If there are additional test cases copy them as `a1`, `a2` etc.
- (I am considering to use some automated tools to download test examples)

### How to use (Python)

To run the code
- For python, use `python a.py < a0`

The debug statements prints in a different color.
You can submit the code without commenting out the debugging statements, I do not think it should affect the run time.

To compile the code and run for all test cases

```
./run_py.sh a
```

You can set up and alias for the script and just run something like `px a`

##### Recursion

If you need to recursively call functions more than 1000 times, please use the function decorator in `recursive_example_1.py`.

##### Interactive questions
- You can use the input as usual (please check)
- When printing, please flush, i.e. `print(x, flush=True)`
- At the end of the program, execute `sys.exit()`
- Failing the sample test usually will not incur penalty time.

##### Algorithm Templates 
The following algorithmic templates should be available.

- [AtCoder library](https://atcoder.github.io/ac-library/master/document_en/) 
  - (There is a [Python](https://github.com/not522/ac-library-python) [version](https://github.com/Mitarushi/ACL-Python) but probably I want to extract copiable snippets instead of running the script to transfer the functions.
- Math
  - Ceiling division (ok)
  - Inverse modulo (ok)
  - Prime factorisation (ok)
  - Chinese Remainder Theorem (please check)
  - Floor Sum
  - Convolution
  - Binomial coefficient
- Trees
  - Trie (ok)
  - Fenwick Tree
  - Segment Tree
  - Lazy Segment Tree
  - [intervaltree](https://github.com/chaimleib/intervaltree) clone
  - [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) clone
- Arrays
  - Prefix Sum
  - Longest Common Subsequence (ok)
  - Longest Common Subarray (ok)
  - Longest Increasing Subsequence (ok)
  - Sliding Windows
  - Suffix Array
  - LCP array
  - Z algorithm
- Search
  - Binary Search
  - Ternary Search
  - [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html)
  - Gradient Descent
- Graphs
  - (Some code to process graphs)
  - Dijkstra Algorithm (ok)
  - Count Connected Components (ok)
  - Disjoint Set Union (ok)
  - Minimum Spanning Tree (ok)
  - Topological Sort and Cycle Detection (ok)
  - Clique Cover and Chromatic Number (ok)
  - Floyd–Warshall algorithm (tbc, for graphs with negative edges)
  - Dinic's algorithm for max-flow problem (tbc)
  - Algorithm (?) for min-cost flow problem (tbc)
  - 2-SAT (tbc)
- Recursion template
  - (Because the default recursion limit for Python is 1000)
- Other Algorithms
  - Convex Hull (tbc, Monotone Chain algorithm)
  - Coordinate Compression (tbc)


### How to use (C++)

Please refer to my [C++ conversion course](../docs/cpp_conversion_course.md)

To compile the code and run for all test cases

```
./run_cpp.sh x
```

You can set up and alias for the script and just run something like `cx x`

## Wishlist

Understand the tricks of using C++
- Understand the basics first
- Compiler optimisation
- Probably I would never implement advanced data structures for Grandmaster+ rankings

Procedure to automatically download test cases
- Currently I copy and paste to the respective places and run them individually.

Algorithm templates as above

CI/CD to check correctness and runtime of algorithm templates

## Resources

Recently I found a [competitive programing library in Python](https://github.com/cheran-senthil/PyRival).
- I think I will continue developing this because it also saves all my participation attempts, and I want folders and files to navigate through.
- Some code will be copied from there, I will change them to fit my style.