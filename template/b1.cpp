def solve_(n, arr_original):
    # your solution here

    res = 0

    for i in range(n):
        for j in range(i+1, n+1):
            arr = arr_original[i:j]

            pos = {x:i for i,x in enumerate(arr)}

            brr = sorted(arr)

            crr = [pos[x] for x in brr]

            # log(crr)

            left = 0
            right = 0
            count = 0
            for i,x in enumerate(crr):
                right = max(right, x)
                if right == i:
                    # log(left, right)
                    if right > left:
                        count += right - left
                    left = i+1
            
            # log(arr, crr, count)
            res += count

    return res


for case_num in range(int(input())):

    n = int(input())
    arr = list(map(int,input().split()))
    res = solve(n, arr)  # include input here
    print(res)