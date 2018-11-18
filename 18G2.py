file = open("B-small-attempt1.in", "r") 
lines = file.read().splitlines()

tests_total = int(lines[0])
tests = []
test_number = 1

i = 1
while i < len(lines):
    num_list = list(lines[i+1])
    num_list = [int(num) for num in num_list]
    
    tests.append((test_number, num_list))
    
    i += 2
    test_number += 1

print(tests)


def test_function(test):
    test_number, b_list = test

    values = []
    for i,b in enumerate(b_list):
        # going right, destroys from right
        rightest_index = int((len(b_list)+i)/2+0.5)-1
        going_right = sum(b_list[i:rightest_index+1])
        values.append(going_right)

        # going left, destroys from left
        leftest_index = int((i/2+0.5))
        going_left = sum((b_list[leftest_index:i+1]))
        values.append(going_left)

#         print(leftest_index,rightest_index)

        sub_list = b_list[leftest_index:rightest_index+1]
        if rightest_index - leftest_index +1 >= len(b_list)/2:
            for j in range(rightest_index-int(len(b_list)/2)+1):
                spread = sub_list[j:j+int(len(b_list)/2+1)]
    #             print(sum(spread))
                values.append(sum(spread)%(7+10**9))

    count = max(values)
#     print(count)
    return test_number, count


with open("18G2.out", "w") as f:
    for test in tests:
        test_number, count = test_function(test)
        print("Case #{}: {}".format(test_number, count))
        f.writelines("Case #{}: {}\n".format(test_number, count))