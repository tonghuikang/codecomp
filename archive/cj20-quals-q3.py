def solve(matrix):
    matrix = sorted(matrix)
    res = [0 for _ in matrix]
    
    current_time = 0
    
    for start,end,i in matrix:
#         print(i,start,end)
        if start < current_time:
            continue
        res[i] = 1
        current_time = end
    
    current_time = 0
    
#     print(res)
#   print(matrix)
    
    for start,end,i in matrix:
        if res[i] == 0:
            if start < current_time:
                return "IMPOSSIBLE"
            current_time = end      
            
    return "".join(["C" if r == 1 else "J" for r in res])


str_input = input()
cases = int(str_input)

for case_num in range(1, cases+1):
    arr_all = []
    
    str_input = input()
    nrows = int(str_input)
    
    matrix = []
    for i in range(nrows):
        str_input = input()
        matrix.append([int(x) for x in str_input.split()] + [i])
    
    str_output = solve(matrix)
    
    print("Case #{}: {}".format(case_num, str_output))