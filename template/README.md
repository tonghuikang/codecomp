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

##### Recursion

If you need to recursively call functions more than 1000 times, please use the function decorator in `recursive_example_1.py`.

##### Interactive questions
- You can use the input as usual (please check)
- When printing, please flush, i.e. `print(x, flush=True)`
- At the end of the program, execute `sys.exit()`
- Failing the sample test usually will not incur penalty time.

##### Algorithm Templates 
The following algorithmic templates should be available.

- Convex Hull (tbc, Monotone Chain algorithm)
- Coordinate Compression (tbc)
- [intervaltree](https://github.com/chaimleib/intervaltree) clone
- [sortedcontainers](https://github.com/grantjenks/python-sortedcontainers) clone
- [AtCoder library](https://atcoder.github.io/ac-library/master/document_en/) 
  - (There is a [Python](https://github.com/not522/ac-library-python) [version](https://github.com/Mitarushi/ACL-Python) but probably I want to extract copiable snippets instead of running the script to transfer the functions.
  - Math
    - Inverse modulo and power modulo (should have been somewhere already)
    - Chinese Remainder Theorem
    - Floor Sum?
    - Convolution
  - Data Structures
    - Fenwick Tree
    - Segment Tree
    - Lazy Segment Tree
    - Strings
      - Suffix Array
      - LCP array
      - Z algorithm
  - Graphs
    - (Some code to process graphs)
    - Dijkstra Algorithm (ok)
    - Count Connected Components (ok)
    - Disjoint Set Union (ok)
    - Minimum Spanning Tree (ok)
    - Topological Sort and Cycle Detection (ok)
    - Floyd–Warshall algorithm (tbc, for graphs with negative edges)
    - Dinic's algorithm for max-flow problem (tbc)
    - Algorithm (?) for min-cost flow problem (tbc)
    - 2-SAT

### How to use (C++)

(tbc)


## Wishlist

Understand the tricks of using C++
- Understand the basics first
- Compiler optimisation
- Probably I would never implement advanced data structures for Grandmaster+ rankings

Procedure to automatically download test cases
- Currently I copy and paste to the respective places and run them individually.

Algorithm templates as above

Procedure to run test cases automatically
- Ideally I want to run all the test cases at once with a command.
- Bonus if it compares to the expected test cases.

CI/CD to check correctness and runtime of algorithm templates