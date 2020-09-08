import sys
size = int(input())

if size == 1:
    print("! 1",flush = True)
    sys.exit()

arr = [None for _ in range(size+1)]

print ("? 1 2",flush = True)   # p1 mod p2  if res larger, p1 = val, p2 > p1
val_1 = int(input())

print ("? 2 1",flush = True)   # p2 mod p1
val_2 = int(input())

if val_1 > val_2:
    large_idx = 2
    arr[1] = val_1
else:
    large_idx = 1
    arr[2] = val_2

# if size == 2:
#     if large_idx == 2:
#         print("! 1 2",flush = True)
#     else:
#         print("! 2 1",flush = True)
#     sys.exit()

for i in range(2+1, size+1):
    print("? {} {}".format(i, large_idx),flush = True)
    if 


