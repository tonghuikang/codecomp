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
The problems are well-written and usually is not a mere duplicate of what you can find on the Internet.
There are four questions. The first question is simple. 
The next three questions are more difficult and its difficult varies.

One question is on binary trees, or uses binary trees. Some training is necessary to understand how to use them. Binary trees are constructed from an array and can be deconstructed and be represented by an array.


# Regarding codejam
I am far from being qualified into the top 1500 of CodeJam round 1.

On the use of Python. One main reason I want to use Python is because the rest of the school (SUTD) is only familar with Python. I want to make a starter kit to make it easy to participate in Codejam/Kickstart which takes in line input and output. A lot of time is wasted not writing the function.

## What to include in starter kit / template code
- Automatic loading and typing
- Print statements to inspect variables (considering pysnooper)
- Default case printing

## How to participate in interactive questions
- Downlaod the testing tool specific to the question and the general interactive runner.
```python interactive_runner.py python testing_tool.py 0 -- ./solution_q1.py```
- Remember to add a shebang at the start of the code
```#!/usr/bin/env python```

## Tips
- Use multiple screen. Put the problem in another screen for easy viewing and testing
- Use a proper IDE? Currently my workflow is jupyter > copy cell and paste to a .py, test locally if applicable, upload to codejam and test
- 

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
