str_input = input()
cases = int(str_input)

for case_num in range(1, cases+1):
    arr_all = []
    
    str_input = input()
    lst = [int(x) for x in str_input]
    
    indicator = 0
    
    res = ""
    
    for bit in lst:
        change = int(bit) - indicator
        if change > 0:
            res += "("*change
        if change < 0:
            res += ")"*-change
        res += str(bit)
        indicator = int(bit)
   
    change = 0 - indicator
    if change > 0:
        res += "("*change
    if change < 0:
        res += ")"*-change
                
    print("Case #{}: {}".format(case_num, res))