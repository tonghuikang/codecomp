# Leetcode Python Reference


## Overview of this reference

This guide is will be an overview of concepts for people who have never taken a course on algorithms (like me). 

I use Python because I am more familiar with it.

All leetcode problems should be solvable with Python as well, because the question is very constrained. However, in coding competitions (like one you need to deploy an API that solves incoming challenges), the speed at which Python creates objects can be too slow.

This contains
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


## Leetcode setup

A sample function looks like this

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

Writing on Leetcode|Writing on local computer 
-----------------------------|--------------------------------------
No need to copy and paste anything.|**Require copying of starter code and test cases**, which might have error.
Debugging requires print statements.|**Dubugging tools** is available with your IDE
**Waiting time for the code to run**.|No waiting time.
A **cooldown** applies between running code.|No cooldown or limits.
**Submission** is easy, and there is a greater confidence that it works.|Requires copying to leetcode for submission. Copying might cause error again.
Shows **expected output** (not during competitions)|Does not show expected output.
Require manual work to **swtich between test cases**.|Test cases (and its results) can be saved and tested all at once.

In summary, writing on Leetcode is great if you are confident that your code will work in one sitting - this especially applies to the easy question. However, if you code involve extensive debugging, perhaps it might be better to bring your code offline.

## Code snippets

These are some code snippets I freqently use in Leetcode, in descending order. I place them here so that I do not need to use the search engine everytime I want it.

**Sorting a 2D list based on a certain index**. <br>
https://stackoverflow.com/questions/18563680/ <br>

```python
lst = sorted(lst,key=lambda e:e[1])
```


**Making a freqency dictionary.** <br>
https://stackoverflow.com/questions/722697/ <br>
```python
from collections import defaultdict
fq = defaultdict(int)
for w in words:
    fq[w] += 1
```

```python
from collections import Counter
fq = Counter(lst)
```



### Graphs

There are a few types of graphs
- depending whether it is directed or undirected
- whether the nodes are weighted,
- whether the edges are weighted.



**Creating a unweighted <u>directed</u> graph**<br>

```python
from collections import defaultdict

class Graph: 
    def __init__(self,vertices): 
        # dictionary containing adjacency List 
        self.graph = defaultdict(list) 
        # number of vertices
        self.V = vertices  
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def additionalFunction(self,u,v):
        return None
```

Usage of the Graph object.

```python
g = Graph(6) 
g.addEdge(5, 2) 
g.addEdge(5, 0) 
g.addEdge(4, 0)
g.additionalFunction() 
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





# Additonal notes recorded

Sometimes, it is better to write a probabilitistic algorithm with a small but calculated chance the algorithm fails.



Difference between substring and subsequence

Lexicographic (not alphabetical) order - is ab > aaa > aa? yes (cite leetcode questions)

On whether should we care about



### Common algorithms
(please elaborate - given what, produce what)

Dijkstra

Minimum spanning tree








### How to write recursive algorithms

You need two functions, one to start, one to call.


### Tricks
You can define a function within a function. 
You can define a function outside, but sometimes the function is inside an object, then you need to use the `self` which complicate matters.



### Complexity concepts
You need to roughly calculate the worst case scenario - consider how much computations is necessary.

Hashmap read is much faster than ?.

Binary search insert is faster because there is no need to read the whole (sorted) array.


### Misc
Bitwise operations.


### Python
del lst[0] is efficient, but lst = lst[1:] requires iterating through the full array.





# Regarding competitive coding in general
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


# Regarding leetcode
There is a leetcode contest every Sunday. It starts at 10:30 am Singapore time and lasts for 90 minutes. 

The problems are usually well-written and usually are not a mere duplicate of what you can find on the Internet.
There are four questions. The first question is simple. 
The next three questions are more difficult and its difficulty varies.

One question is on binary trees, or uses binary trees. Some training is necessary to understand how to use them. Binary trees are constructed from an array and can be deconstructed and be represented by an array.


# Regarding codejam
I am far from being qualified into the top 1500 of CodeJam round 1.

On the use of Python. One main reason I want to use Python is because the rest of the school (SUTD) is only familar with Python. I want to make a starter kit to make it easy to participate in Codejam/Kickstart which takes in line input and output. A lot of time is wasted not writing the function.

## What to include in starter kit / template code
- Automatic loading and typing
- Debugging tools 
  - To try out VScode or pysnooper?

## How to participate in interactive questions
- Downlaod the testing tool specific to the question and the general interactive runner. (official reference?)
```python interactive_runner.py python testing_tool.py 0 -- ./solution_q1.py```
- Remember to add a shebang at the start of the code
```#!/usr/bin/env python```

## Tips
- Use multiple screens. Put the problem in another screen for easy viewing and testing.
- Use a proper IDE? Currently my workflow is jupyter > copy cell and paste to a .py, test locally if applicable, upload to codejam and test

# I got zero for this :(
Question 1 I could not find out my errors. Question 2 the code took too long to run (it generates 1GB of memory) and my answers is wrong also.

# Reflections
I should not be using Python for any coding challenge. It is too slow.

Moreover, if I am using Python, I need to have a standard process to read and write files. I spent quite some time hand-copying test cases to the notebook input space. Next time I should just simply read file instead, and I do not need to get out of notebook, other than submitting code.

Multiprocessing. On my computer I could only run 37 cases for question 2. I can select a 24 or 96 vCPU cloud and run the cases in parallel. It works (though my code produce the wrong result). Following is the installation script for your cloud:
```curl https://raw.githubusercontent.com/tonghuikang/kickstart/master/install.sh | sudo bash```

Now I will analyse why my answers are wrong :/

# Question Analysis
For Question 1, I have missed the special case of zeros. What I did is to multiply two numbers count how many numbers are equal to the result. To make the code run slightly faster I first sort them and the see if any of the larger number is the product of the first two numbers. However, the triplet of `(0,0,100)` works as `0*100=0` but it isn't included in our system - as well as `(1,99,99)` as `1*99=99`. To solve the large problem, you need to use hash tables and collections - i.e. grouping the numbers with the same value together. Libraries like `collections` and `deque` seem to be essential before you can claim that you work with Python. Even with my revised code, I need 24 vCPU on GCP to solve the problem in time.

I could not find out where I am wrong in Question 2. (Probably everything) The code provided by Python writer xjcl does not work: https://code.google.com/codejam/contest/5374486/scoreboard?c=5374486#vf=1&sp=331 
This person also seem to follow a standard debugging procedure, separating print to file and printing on console. I hope to develop an SOP for the next Google kickstart.

# Google Kickstart 2018 Round G

### Why Python? (I retract this - ALWAYS USE .CPP FOR CODEJAM/KICKSTART)
Because I have been coding in Python. The intermediate results are saved and be easily be shown to other people. Moreover I am not yet in the business of optimising yet. I am not sure for Google Kickstart/CodeJam but I know that Hackerrank allow more run time for files written in Python.

The use of Python was an issue in a recent coding challenge at Credit Suisse. Python was slow, which is suspect is due to all the deepcopy that needs to be made. Someday, I need to have some understanding of C++ does. 


# On the use of code from the Internet

From https://code.google.com/codejam/resources/faq:

> During the round, can I use code written before the round?
> As long as you have a license to use it, yes. That means you can write your own helper code, or collect your own personal library of code, as long as the license terms of the code permit it. Some Code Jam contestants will have competed on an ACM ICPC team, and many of those teams have their own code books; check with your team's coach whether it's permissible for you to use that code in a different context.

I guess I will simply use what I can find on the Internet for this competition. I should be expected to write from functions like sort algorithms from scratch.

Sometimes the code from the Internet is faulty as well. "ABB" and "BAB" are anagrams of each other, but https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/ detects otherwise.

> What is considered cheating?
> See Section 7 (Disqualification) of the Terms and Conditions and Section 7 (Disqualification) of the Contest Rules.
> Collaborating with anyone else during any round of the contest, with the exception of the Qualification Round or Practice Session, is strictly prohibited and will result in your disqualification. This includes discussing or sharing the problem statements or solutions with others during the round. Participating with multiple accounts is also prohibited. If we believe that you have undermined the integrity of the contest, we reserve the right to disqualify you. Use your best judgment. If you have a question about whether something is allowed, or if you suspect another contestant of cheating, please contact us at codejam@google.com.

This repository will only the updated at the end of the competition.

**Recommended leetcode setup**

This is for me to improve my leetcode efficiency. 
I am forgettful and usually lose track of details.

Common mistakes in python - please refer to digital world.
Setup - use VScode to track your variables.

A good programmer does not repeat a mistake.
