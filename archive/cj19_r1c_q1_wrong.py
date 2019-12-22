str_input = input()
str_input_list = str_input.split()
t, = [int(x) for x in str_input_list]  # 1 7 1000000
# 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 

for case_num in range(1, t+1):
    str_input = input()
    str_input_list = str_input.split()
    A, = [int(x) for x in str_input]

    lst = []
    for _ in range(A):
        str_input = input()
        lst.append(str_input)

    res = [[] for _ in range(256)]
    win_map = {"".join(sorted(list(set(["P"])))):"S",
               "".join(sorted(list(set(["R"])))):"P",
               "".join(sorted(list(set(["S"])))):"R",
               "".join(sorted(list(set(["P","R"])))):"P",
               "".join(sorted(list(set(["R","S"])))):"R",
               "".join(sorted(list(set(["S","P"])))):"S",
               "".join(sorted(list(set(["P","R","S"])))):"IMPOSSIBLE"}

    for i in range(256):
        for j in lst:
            res[i].append(j[i%len(j)])
    res = ["".join(sorted(list(set(r)))) for r in res]

    if "".join(sorted(list(set(["P","R","S"])))) in res:
        print("Case #{}: {}".format(case_num, "IMPOSSIBLE"))
    else:
        res_str = "".join([win_map[r] for r in res])
        print("Case #{}: {}".format(case_num, res_str))