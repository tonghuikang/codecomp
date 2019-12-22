from collections import Counter

def q1(case):
    case_num, nums = case
    nums = sorted(nums)
    mp = Counter(nums)
    nonzeros = len(nums) - mp[0]
    counter = int(mp[0] * (mp[0]-1) * (mp[0]-2) / 6) + int(mp[1] * (mp[1]-1) * (mp[1]-2) / 6)  # triplets of 1 and zero
#     print(mp, nonzeros, counter)

    for a in mp:
        val = a*a
        if val != a:
            counter += int(mp[a] * (mp[a]-1) / 2 * mp[val])

        for b in mp:
            if b > a: 
                val = a*b
                if val == a:
                    counter += int(mp[0] * (mp[0]-1) * mp[b]/2)
                if val == b:
                    counter += int(mp[b] * (mp[b]-1) * mp[1]/2)
                if val > b:
                    counter += mp[a] * mp[b] * mp[val]
    return case_num, counter
    
cases = []
t = int(input())  # read a line with a single integer
for case_num in range(1, t + 1):
    dump = int(input())
    arr = [int(s) for s in input().split(" ")]
    cases.append([case_num, arr])

import multiprocessing as mp
n_thread = mp.cpu_count()
with mp.Pool(n_thread) as p:
    results = p.map(q1, cases)

results.sort(key=lambda x: x[0])

for result in results:
    print("Case #{}: {}".format(result[0], result[1]))