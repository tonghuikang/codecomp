def q1(arr):
    arr.sort()
    num_nonzeros = len([x for x in arr if x > 0])
    
    length = len(arr)
    counter = 0
    for i in range(length):
        for j in range(i+1, length):
            if arr[i] == 0 and arr[j] == 0:
                counter += num_nonzeros
            counter += arr[j+1:].count(arr[i]*arr[j])
    return counter


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    dump = int(input())
    arr_a = [int(s) for s in input().split(" ")]
    assert dump == len(arr_a)
    
    result = q1(arr_a)
    print("Case #{}: {}".format(i, result))