def q1(case):
    case_num, arr = case
    arr.sort()
    num_nonzeros = len([x for x in arr if x > 0])
    
    length = len(arr)
    counter = 0
    for i in range(length):
        for j in range(i+1, length):
            if arr[i] == 0 and arr[j] == 0:
                counter += num_nonzeros
            counter += arr[j+1:].count(arr[i]*arr[j])
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