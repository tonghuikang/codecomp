#!/usr/bin/env python3
import sys
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque
input = sys.stdin.readline  # to read input quickly


# custom imports
# import pandas
# from sklearn.model_selection import train_test_split

# from scipy.optimize import linear_sum_assignment

# import torch
# import keras
# import tensorflow

# import lightgbm
# import xgboost


# available on Google, AtCoder Python3, not available on Codeforces
# import numpy as np
# import scipy

M9 = 10**9 + 7  # 998244353
# d4 = [(1,0),(0,1),(-1,0),(0,-1)]
# d8 = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
# d6 = [(2,0),(1,1),(-1,1),(-2,0),(-1,-1),(1,-1)]  # hexagonal layout
MAXINT = sys.maxsize

# if testing locally, print to terminal with a different color
OFFLINE_TEST = True  # quora does not allow getpass
# OFFLINE_TEST = False  # quora does not allow getpass
def log(*args):
    if OFFLINE_TEST:
        print('\033[36m', *args, '\033[0m', file=sys.stderr)

def solve(*args):
    # screen input
    if OFFLINE_TEST:
        log("----- solving ------")
        log(*args)
        log("----- ------- ------")
    return solve_(*args)

def read_matrix(rows):
    return [[x-1 for x in list(map(int,input().split()))] for _ in range(rows)]

def read_strings(rows):
    return [input().strip() for _ in range(rows)]

# ---------------------------- template ends here ----------------------------


def solve_(m,story_creator,user_follow_user,user_follow_story):
    # your solution here

    map_story_to_creator = {story:user for story,user in enumerate(story_creator)}

    map_user_to_created_stories = defaultdict(set)
    for story,user in enumerate(story_creator):
        map_user_to_created_stories[user].add(story)

    map_story_to_followers = defaultdict(set)
    map_user_to_followed_stories = defaultdict(set)
    for user,story in user_follow_story:
        map_user_to_followed_stories[user].add(story)
        map_story_to_followers[story].add(user)

    map_user_to_following_user_direct = defaultdict(set)
    for user_following,user_followed in user_follow_user:
        map_user_to_following_user_direct[user_following].add(user_followed)

    map_user_to_following_user_create = defaultdict(set)
    for user in range(m):
        stories_followed = map_user_to_followed_stories[user]
        for story in stories_followed:
            map_user_to_following_user_create[user].add(map_story_to_creator[story])

    map_user_to_following_user_follow = defaultdict(set)
    for user in range(m):
        stories_followed = map_user_to_followed_stories[user]
        for story in stories_followed:
            map_user_to_following_user_follow[user].update(map_story_to_followers[story])

    for user_i in range(m):
        scoring = [0 for _ in story_creator]  # default scoring

        for user_j in range(m):
            if user_i == user_j:
                continue
        
            multiplier = 0
            if user_j in map_user_to_following_user_direct[user_i]:
                multiplier = 3

            elif user_j in map_user_to_following_user_create[user_i]:
                multiplier = 2

            elif user_j in map_user_to_following_user_follow[user_i]:
                multiplier = 1

            for story in range(len(story_creator)):
                if story in map_user_to_created_stories[user_j]:
                    scoring[story] += multiplier*2
                elif story in map_user_to_followed_stories[user_j]:
                    scoring[story] += multiplier*1

        # score -1 - user already follow or create the story
        for story in map_user_to_followed_stories[user_i]:  # -1
            scoring[story] = -1
        for story in map_user_to_created_stories[user_i]:  # -1
            scoring[story] = -1

        log(user_i, scoring)
        res = sorted((score,-i) for i,score in enumerate(scoring))[::-1]
        print(*[-i+1 for score,i in res][:3])
    
    return


for case_num in [0]:  # no loop over test case
# for case_num in range(100):  # if the number of test cases is specified
# for case_num in range(int(input())):

   
    # read one line and parse each word as an integer
    n,m = list(map(int,input().split()))
    story_creator = []
    for i in range(n):
        story_creator.append(int(input())-1)

    p,q = list(map(int,input().split()))
    user_follow_user = read_matrix(p)  # and return as a list of list of int
    user_follow_story = read_matrix(q)  # and return as a list of list of int

    # read multiple rows
    # mrr = read_matrix(k)  # and return as a list of list of int
    # arr = read_strings(k)  # and return as a list of str

    res = solve(m,story_creator,user_follow_user,user_follow_story)  # include input here
    
    # print result
    # Google and Facebook - case number required
    # print("Case #{}: {}".format(case_num+1, res))

    # Other platforms - no case number required
    # print(res)
    # print(len(res))
    # print(*res)  # print a list with elements
    # for r in res:  # print each list in a different line
        # print(res)
        # print(*res)