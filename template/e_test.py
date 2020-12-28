CASES = 976
print(CASES)
cnt = 0
for i in range(CASES):
    srr = "1"*i + "0"*(i+30)
    print("{} {}".format(len(srr), i+1))
    print("{}".format(srr))
    cnt += len(srr)
# print(cnt)