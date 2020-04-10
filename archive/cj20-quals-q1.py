def solve(matrix):
    
    trace = sum([row[i] for i,row in enumerate(matrix)])
    
    row_cnt = 0
    for row in matrix:
        if sorted(list(set(row))) != sorted(row):
            row_cnt += 1

    matrix = zip(*matrix)
    
    col_cnt = 0
    for row in matrix:
        if sorted(list(set(row))) != sorted(row):
            col_cnt += 1
    
    return trace, row_cnt, col_cnt
    

str_input = input()
cases = int(str_input)

for case_num in range(1, cases+1):
    arr_all = []
    
    str_input = input()
    nrows = int(str_input)
    
    matrix = []
    for _ in range(nrows):
        str_input = input()
        matrix.append([int(x) for x in str_input.split()])
    
    trace, row_cnt, col_cnt = solve(matrix)
    
    print("Case #{}: {} {} {}".format(case_num, trace, row_cnt, col_cnt))