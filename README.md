## Overview of this reference



Python snippet gallery
- [Python](python.md)

Mathematical theories
- [Geometry](geometry.md)
- [Number theory](number_theory.md)
- [Probability](Probability)

Methods
- [Binary search](binary_search.md)
- [Bit manipulation](bit_manipulation.md)
- [Dynamic programming](dynamic_programming.md)

Specific problems
- [Optimisation](optimisation.md)
- [Named problems](specific_problems.md)

Data structures
- [Graphs](graphs.md)
- [Trees](tree.md)





Miscellaneous
- [Websites](websites.md)
- [Interview](interview.md)

  


**What this document contains** (to be updated)

- a reference to terminologies used in leetcode
- code snippets
- problems and their named solutions and implementation

**What this is not**

This does not teach you Python. Neither does this teach or algorithms. There is no step-by-step guide here.

This does not help you with anything other than helping people like me perform better at leetcode. For the full technical interview process please do refer to Yangshun's [tech interview handbook](https://yangshun.github.io/tech-interview-handbook), which I think it covers all aspects of the technical interview.


## Foreword

Spending one or two one-and-half hours every week on solving programming problems is pretty fun. I can see myself playing leetcode for a long time.

There are code snippets and references that would have helped me to become more efficient at coding. Here I am sharing with you what I have done for myself.

Moreover, many big companies have a coding interview at various stages of hiring. If entering these companies is your objective it is recommended that you are good at solving problems.

Of course, this is not enough to get hired. In the interview you need to clarify the problem, explain your approach and then justify the computational complexity, without being affected by the interview setting.

We also have to keep in mind the more important prerequsites of a good hire 
- good communication skills
- good discipline at work 
- ability to learn quickly

Why is Leetcode better? It offers weekly challenges which I am keen to participate. Moreover, it handles the input/output for you so that you can focus on the code that matters. (On the other hand, for CodeForces or Google CodeJam, you are required to parse the text input, which can be time consuming and error prone.)

This guide is will be an overview of concepts for people who have never taken a course on algorithms (like me). 

I use Python because I am more familiar with it.

All leetcode problems should be solvable with Python as well, because the question is very constrained. However, in coding competitions (like one you need to deploy an API that solves incoming challenges), the speed at which Python creates objects can be too slow.

**On problem solving**

This is this process to follow
- Understand the question
- Formula solution strategy
- Implement solution strategy
- Deliver solution

There are some insights to understanding this ideal process.
- Each step depends on the previous steps.
  - You cannot implement the solution without formulating a strategy. 
  - You cannot devise a strategy without understanding the question.
  - It may be possible that you understand the question wrong, and wasted time on the rest of the steps.
- Having a strategy does not mean that you have the ability to implement it.


## Leetcode setup

A starter code on Leetcode looks like this

```python
class Solution:
    def functionName(self, s: str) -> str:
        return s
```

If you are to run the code on your computer, this is how you check the result.

```
s = Solution()
print(s.functionName("test_string"))
```

[TODO: Consider the use of PySnooper here]

Here we consider the advantages and disadvantages of testing on your computer (for example writing on VSCode with a debugger)

| Writing on Leetcode                                          | Writing on local computer                                    |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| No need to copy and paste anything.                          | **Require copying of starter code and test cases**, which might have error. |
| Debugging requires print statements.                         | **Dubugging tools** is available with your IDE               |
| **Waiting time for the code to run**.                        | No waiting time.                                             |
| A **cooldown** applies between running code.                 | No cooldown or limits.                                       |
| **Submission** is easy, and there is a greater confidence that it works. | Requires copying to leetcode for submission. Copying might cause error again. |
| Shows **expected output** (not during competitions)          | Does not show expected output.                               |
| Require manual work to **swtich between test cases**.        | Test cases (and its results) can be saved and tested all at once. |

In summary, writing on Leetcode is great if you are confident that your code will work in one sitting - this especially applies to the easy question. However, if you code involve extensive debugging, perhaps it might be better to bring your code offline.

## Terminologies

Difference between subset, subsequence and subarray/substring
- subset: some elements in the collection
- subsequence: some elements in the array maintaining relative order (not necessary to be continuous)
- subarray: some continuous elements in the array

Lexicographic (not alphabetical) order - is ab > aaa > aa? yes (cite leetcode questions)