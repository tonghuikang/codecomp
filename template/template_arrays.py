#!/usr/bin/env python3
import sys, os, getpass
import math, random
import functools, itertools, collections, heapq, bisect
from collections import Counter, defaultdict, deque

MAXINT = sys.maxsize

# ------------------------ standard imports ends here ------------------------


# ------------------------- helper functions ----------------------------


def prefix_sum(arr):
    psum = [0]
    for x in arr:
        psum.append(psum[-1] + x)
    return psum


def prefix_sum2(arr):
    psum = [0]
    psum2 = [0]
    for x in arr:
        psum.append(psum[-1] + x)
        psum2.append(psum2[-1] + psum[-1])
    return psum2


def powerset(iterable):
    # https://stackoverflow.com/a/18035641/5894029
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def colorings(iterable):
    # https://stackoverflow.com/questions/20549341/ not very related
    raise NotImplementedError


def remove_consecutive_duplicates(lst):
    res = []
    for x in lst:
        if res and x == res[-1]:
            continue
        res.append(x)
    return res


def split_by_same_elements(lst):
    res = []
    for x in lst:
        if res and x == res[-1][0]:
            res[-1][-1] += 1
            continue
        res.append([x, 1])
    return res


def split_into_number_and_char(srr):
    import re

    # https://stackoverflow.com/q/430079/5894029
    # numbers are grouped together
    arr = []
    for word in re.split("(\d+)", srr):
        try:
            num = int(word)
            arr.append(num)
        except ValueError:
            for c in word:
                arr.append(c)
    return arr


def interval_overlap(x1, x2, y1, y2):
    # given intervals [x1,x2], [y1,y2]
    # [start, end] of overlapping interval
    # if start > end, there is no overlapping inteval
    return max(x1, y1), min(x2, y2)


def combine_overlapping_intervals(intervals):
    # https://leetcode.com/problems/count-the-number-of-good-partitions/
    intervals.sort()
    new_intervals = []

    for a,b in intervals:
        if new_intervals and a <= new_intervals[-1][1]:
            # please check if you intend to combine for equality
            new_intervals[-1][1] = max(new_intervals[-1][1], b)
        else:
            new_intervals.append([a,b])
            
    return new_intervals


def count_peaks_and_valleys(lst):
    # leetcode.com/problems/count-hills-and-valleys-in-an-array/
    if len(lst) <= 2:
        return 0, 0
    peaks = 0
    valleys = 0
    for a, b, c in zip(lst, lst[1:], lst[2:]):
        if a < b and b > c:
            peaks += 1
        if a > b and b < c:
            valleys += 1
    return peaks, valleys


def is_subsequence(self, s, t) -> bool:
    # https://leetcode.com/problems/is-subsequence/
    if len(s) == 0:
        return True

    l = 0
    for r in range(len(t)):
        if t[r] == s[l]:
            l += 1
        if l == len(s):
            return True

    return False


def split_when_different(lst):
    res = []
    cur = []

    for x in lst:
        if cur and x == cur[-1]:
            cur.append(x)
        else:
            if cur:
                res.append(cur)
            cur = [x]
    if cur:
        res.append(cur)
    return res


def two_pointers(arr, entry_func, exit_func, condition):
    # number of subarrays that passes condition

    nonlocal cnt
    n = len(arr)
    # entry_func(right) -> None
    # exit_func(left) -> None
    # condition() -> bool

    res = 0
    right = 0
    for left in range(n):
        # advance until condition passes
        while right < n and not condition():
            entry_func(right)
            right += 1
        if condition():  # possible that right == n and not pass
            res += n - right + 1
        exit_func(left)
    return res


# def entry_func(right):
#     nonlocal cnt
#     x = nums[right]
#     prev = cntr[x]
#     cntr[x] += 1
#     after = cntr[x]
#     diff = (after * (after-1) // 2) - (prev * (prev-1) // 2)
#     cnt += diff

# def exit_func(left):
#     nonlocal cnt
#     x = nums[left]
#     prev = cntr[x]
#     cntr[x] -= 1
#     after = cntr[x]
#     diff = (after * (after-1) // 2) - (prev * (prev-1) // 2)
#     cnt += diff

# def condition():
#     return cnt >= k

# cntr = Counter()
# cnt = 0
# res = two_pointers(nums, entry_func, exit_func, condition)


def gathering_cost(xpos):
    # the cost to gather every item to each location
    xpos = sorted(xpos)
    n = len(xpos)
    left_cost = 0
    right_cost = sum([x - xpos[0] for x in xpos])
    cost_arr = [right_cost]

    for i, (prev, nex) in enumerate(zip(xpos, xpos[1:])):
        left_cost += (i + 1) * (nex - prev)
        right_cost -= (n - i - 1) * (nex - prev)
        cost_arr.append(left_cost + right_cost)
    return cost_arr


def gathering_cost_query(xpos, psum, l, m, r):
    # the gathering cost for subarray xpos[l:r+1] onto xpos[m]
    # https://leetcode.cn/problems/apply-operations-to-maximize-frequency-score/
    # https://leetcode.cn/circle/discuss/BYHexE/view/HRjJZC/
    # psum is preprocessed from xpos
    # psum = list(itertools.accumulate(arr, initial=0))
    left = xpos[m] * (m - l) - (psum[m] - psum[l])
    right = psum[r + 1] - psum[m + 1] - xpos[m] * (r - m)
    return left + right


def gathering_cost(xpos):
    xpos = sorted(xpos)
    psum = list(itertools.accumulate(xpos, initial=0))
    return [gathering_cost_query(xpos, psum, 0, m, len(xpos)-1) for m in range(len(xpos))]


def all_nearest_smaller_values(arr):
    # https://en.wikipedia.org/wiki/All_nearest_smaller_values
    # https://leetcode.cn/contest/weekly-contest-358/problems/apply-operations-to-maximize-score/
    # https://poe.com/s/Kc2gVwLTM4hZZJ4EJDOg
    result = [-1 for _ in range(len(arr))]
    stack = []

    for i in range(len(arr)):
        while stack and stack[-1][0] >= arr[i]:  # change this if you want to include equalitys
            stack.pop()
        if stack:
            result[i] = stack[-1][1]
        stack.append((arr[i], i))

    return result


def rabin_karp(arr, window_size, modulus):
    # return all hashes of each substring of a certain window_size
    # run this multiple times to avoid hash collisions
    h, t, d = (1 << (17 * window_size - 17)) % modulus, 0, 1 << 17
    all_hashes = set()

    for i in range(window_size):
        t = (d * t + arr[i]) % modulus

    all_hashes.add(t)

    for i in range(len(arr) - window_size):
        t = (d * (t - arr[i] * h) + arr[i + window_size]) % modulus
        all_hashes.add(t)

    return all_hashes


def sort_deques(deques):
    # in place sort
    # allow big-small merge
    # O((sum(k) - max(k)) * log(n))
    deques.sort()


def join_deques(deques):
    # modifies and returns the largest deque
    # https://leetcode.cn/problems/qoQAMX/
    # allow big-small merge
    # O(sum(k) - max(k))
    if not deques:
        return deque([])

    maxlen = 0
    maxidx = 0
    for i, dq in enumerate(deques):
        if len(dq) > maxlen:
            maxlen = len(dq)
            maxidx = i

    ptr = deques[maxidx]

    for left in deques[:maxidx][::-1]:
        left.reverse()
        ptr.extendleft(left)

    for right in deques[maxidx + 1 :]:
        ptr.extend(right)

    return ptr


def can_partition_array_into_equal_subset_sum(arr):
    # https://codeforces.com/contest/1839/submission/208368758
    total_sum = sum(arr)

    if total_sum % 2 != 0:
        return False

    target_sum = total_sum // 2
    n = len(arr)

    dp = [False] * (target_sum + 1)
    dp[0] = True

    for num in arr:
        for j in range(target_sum, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target_sum]


def find_equal_subset_sum_subset(arr):
    # https://codeforces.com/contest/1839/submission/208368758
    # assuming you can
    # GPT-4 generated, should be optimized
    total_sum = sum(arr)
    target_sum = total_sum // 2
    n = len(arr)

    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] = dp[i][j] or dp[i - 1][j - arr[i - 1]]

    subset = []
    i, j = n, target_sum
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            subset.append(arr[i - 1])
            j -= arr[i - 1]
        i -= 1

    left = subset

    c = Counter(left)
    right = []
    for x in arr:
        log(x, c[x])
        if c[x] > 0:
            c[x] -= 1
            continue
        right.append(x)

    log(sum(left), sum(right), sum(arr))
    assert sum(left) == sum(right)
    assert sum(left) + sum(right) == sum(arr)
    assert sorted(left + right) == sorted(arr)
    return left, right


# ---------------------- longest subsequence or subarray ----------------------


def longest_common_subsequence(arr, brr):
    # leetcode.com/problems/longest-common-subsequence/discuss/351689/
    m, n = map(len, (arr, brr))
    if m < n:
        return longest_common_subsequence(brr, arr)
    dp = [0] * (n + 1)
    for c in arr:
        prevRow, prevRowPrevCol = 0, 0
        for j, d in enumerate(brr):
            prevRow, prevRowPrevCol = dp[j + 1], prevRow
            dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
    return dp[-1]


def longest_common_subarray(arr, brr):
    # binarysearch.com/problems/Longest-Common-Substring
    def slide_along(xrr, yrr):
        maxres = 0
        # slide yrr along xrr
        for i in range(len(xrr)):
            curres = 0  # track current length of common subarray
            for a, b in zip(xrr[i:], yrr):
                if a == b:  # increment if match
                    curres += 1
                    maxres = max(maxres, curres)
                else:  # reset if mismatch
                    curres = 0
        return maxres

    return max(slide_along(arr, brr), slide_along(brr, arr))


def longest_increasing_subsequence(nums):
    # leetcode.com/problems/longest-increasing-subsequence/discuss/667975/
    dp = [MAXINT] * (len(nums) + 1)
    for elem in nums:
        dp[bisect.bisect_left(dp, elem)] = elem
    return dp.index(MAXINT)


def max_dot_product_of_two_subsequence(A, B):
    # leetcode.com/problems/max-dot-product-of-two-subsequences/discuss/648420/
    n, m = len(A), len(B)
    dp = [[0] * (m) for i in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j] = A[i] * B[j]
            if i and j:
                dp[i][j] += max(dp[i - 1][j - 1], 0)
            if i:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if j:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
    return dp[-1][-1]


# ------------------------- lexicographic operations --------------------------


def next_permuation(nums):
    # https://leetcode.com/problems/next-permutation/
    # allow duplicates
    # warning: this algorithm also modifies the input
    k = -1
    # Find the largest index k such that nums[k] < nums[k + 1].
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            k = i

    # If no such index exists, just reverse nums and done.
    if k == -1:
        nums.reverse()
        return

    l = k + 1
    # Find the largest index l > k such that nums[k] < nums[l].
    for i in range(k, len(nums)):
        if nums[k] < nums[i]:
            l = i

    # Swap nums[k] and nums[l]
    nums[k], nums[l] = nums[l], nums[k]

    # Reverse the sub-array nums[k + 1:]
    nums[k + 1 :] = nums[k + 1 :][::-1]
    return nums


def get_permutation_given_lexicographic_order(perm):
    # allow duplicates
    # https://stackoverflow.com/questions/6884708/
    raise NotImplementedError


def get_lexicographic_order_of_permutation(perm):
    # allow duplicates
    # https://www.geeksforgeeks.org/lexicographic-rank-of-a-string/
    # https://www.geeksforgeeks.org/lexicographic-rank-string-duplicate-characters/
    # https://stackoverflow.com/questions/12146910
    # https://stackoverflow.com/questions/6884708/
    raise NotImplementedError


# --------------------------- sliding windows ---------------------------


def sliding_window_sum(nums, k):
    out = [sum(nums[:k])]
    for i in range(k, len(nums)):
        out.append(out[-1] - nums[i - k] + nums[i])
    return out


def sliding_window_maximum(nums, k):
    # leetcode.com/problems/sliding-window-maximum/discuss/65901
    deq, n, ans = deque([0]), len(nums), []
    for i in range(n):
        while deq and deq[0] <= i - k:
            deq.popleft()
        while deq and nums[i] >= nums[deq[-1]]:
            deq.pop()
        deq.append(i)
        ans.append(nums[deq[0]])
    return ans[k - 1 :]


def sliding_window_median(nums, k):
    # leetcode.com/problems/sliding-window-median/discuss/262689
    def move(h1, h2):
        x, i = heapq.heappop(h1)
        heapq.heappush(h2, (-x, i))

    def get_med(h1, h2, k):
        return h2[0][0] * 1.0 if k & 1 else (h2[0][0] - h1[0][0]) / 2.0

    small, large = [], []
    for i, x in enumerate(nums[:k]):
        heapq.heappush(small, (-x, i))
    for _ in range(k - (k >> 1)):
        move(small, large)
    ans = [get_med(small, large, k)]
    for i, x in enumerate(nums[k:]):
        if x >= large[0][0]:
            heapq.heappush(large, (x, i + k))
            if nums[i] <= large[0][0]:
                move(large, small)
        else:
            heapq.heappush(small, (-x, i + k))
            if nums[i] >= large[0][0]:
                move(small, large)
        while small and small[0][1] <= i:
            heapq.heappop(small)
        while large and large[0][1] <= i:
            heapq.heappop(large)
        ans.append(get_med(small, large, k))
    return ans


# ------------------------- largest score -------------------------


def rectangular_submatrix_with_largest_sum(matrix):
    # https://atcoder.jp/contests/abc311/tasks/abc311_g
    # untested O(n3)
    h, w = len(matrix), len(matrix[0])

    maxres = 0
    for i in range(w):
        rowsum = [0 for _ in range(h)]
        # minval = [0 for _ in range(h)]
        for j in range(i, w):
            for x in range(h):
                rowsum[x] += matrix[x][j]
                # minval[x] += min(minval[x], matrix[x][j])
            res = largest_submatrix_sum(rowsum)
            maxres = max(maxres, res)
    return maxres


def largest_submatrix_sum(arr):
    # https://leetcode.com/problems/maximum-subarray/
    val = arr[0]
    maxres = arr[0]

    for x in arr[1:]:
        val = max(x, val + x)
        maxres = max(maxres, val)

    return maxres


def largest_rectangle_in_histogram(heights):
    # https://leetcode.com/problems/largest-rectangle-in-histogram/
    n = len(heights)
    # left boundary => next smaller element to left
    stack = []
    nextSmallerLeft = [0] * n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            nextSmallerLeft[i] = stack[-1] + 1
        stack.append(i)

    # right boundary => next smaller element to right
    stack = []
    nextSmallerRight = [n - 1] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            nextSmallerRight[i] = stack[-1] - 1
        stack.append(i)

    res = heights[0]
    for i in range(n):
        height = heights[i]
        width = nextSmallerRight[i] - nextSmallerLeft[i] + 1
        # width = psum[nextSmallerRight[i]+1] - psum[nextSmallerLeft[i]]
        area = height * width
        res = max(res, area)

    return res


# ------------------------- standard algorithms -------------------------


def z_function(S):
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/z_algorithm.py
    # https://cp-algorithms.com/string/z-function.html
    n = len(S)
    Z = [0] * n
    l = r = 0

    for i in range(1, n):
        z = Z[i - l]
        if i + z >= r:
            z = max(r - i, 0)
            while i + z < n and S[z] == S[i + z]:
                z += 1

            l, r = i, i + z

        Z[i] = z

    Z[0] = n
    return Z


def manachers(S):
    # https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/discuss/1389421/
    # https://github.com/cheran-senthil/PyRival/blob/master/pyrival/strings/suffix_array.py
    # https://cp-algorithms.com/string/suffix-array.html
    A = "@#" + "#".join(S) + "#$"
    Z = [0] * len(A)
    center = right = 0
    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center, right = i, i + Z[i]
    return Z[2:-2:2]


def get_palindromic_ranges(s):
    # https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
    # Tested in https://leetcode.com/problems/palindromic-substrings/submissions/
    # if s is a palindrome, s[1:-1] is also a palindrome
    n = len(s)
    arr = manachers("|" + "|".join(s) + "|")
    bridges = [[] for _ in range(n)]

    for i, x in enumerate(arr):
        start = (i - (x - 2) // 2) // 2
        end = (i + (x - 2) // 2) // 2
        while start <= end:
            bridges[start].append(end + 1)
            start += 1
            end -= 1

    return bridges
