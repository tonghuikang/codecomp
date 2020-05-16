import heapq

def solve(k):

    stack = [(-k,0,k-1)]  # -length, start, end (both inclusive)
    heapq.heapify(stack) 

    res = ["x" for _ in range(k)]
    cnt = 0

    while stack:
        # print(res, stack)
        cnt += 1
        length, start, end = heapq.heappop(stack)
        length = -length  # fix sign
        if length%2 == 1:  # if segment is odd length
            mid_point = (start+end)//2
            res[mid_point] = cnt
            if not start == end:
                heapq.heappush(stack, (-(mid_point-start), start, mid_point-1))
                heapq.heappush(stack, (-(mid_point-start), mid_point+1, end))
        else:  # segment is of even length
            mid_point = (start+end-1)//2
            res[mid_point] = cnt
            if length == 2:  # one other left
                heapq.heappush(stack, (-1, end, end))
            else: 
                heapq.heappush(stack, (-(length//2 - 1), start, mid_point-1))
                heapq.heappush(stack, (-(length//2), mid_point+1, end))

        # if cnt > 5:
        #     break

    # print()
    # print()
    # print()
    return " ".join([str(x) for x in res])
                


strr = input()
for _ in range(int(strr)):
    k = int(input())
    print(solve(k))
