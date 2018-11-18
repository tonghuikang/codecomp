file = open("A-large.in", "r") 
lines = file.read().splitlines()

tests_total = int(lines[0])
tests = []
test_number = 1

i = 1
while i < len(lines):
    info_line = lines[i]
    N, P = info_line.split(" ")
    prefixes = []
    
    for p in range(int(P)):
        prefixes.append(lines[i+p+1])
    tests.append((test_number, int(N), int(P), prefixes))
    
    test_number += 1
    i += int(P) + 1
print(tests)


def test_function(test):

    test_number, N, P, test_prefixes = test
    test_prefixes.sort(key=len)
    # https://stackoverflow.com/questions/4659524/

    lengths = [len(test_prefixes[0])]
    for i,prefix in enumerate(test_prefixes[1:]):
    #     print(i,prefix, test_prefixes[:i+1])
        if not any(prefix.startswith(p) for p in test_prefixes[:i+1]):
            # https://stackoverflow.com/questions/7539959/
            lengths.append(len(prefix))
    # print(lengths)
    count = 2**N - sum([2**(N-length) for length in lengths])
    # print(count)
    return test_number, count


with open("18G1.out", "w") as f:
    for test in tests:
        test_number, count = test_function(test)
        print("Case #{}: {}".format(test_number, count))
        f.writelines("Case #{}: {}\n".format(test_number, count))