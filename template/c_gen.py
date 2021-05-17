import random
random.seed(99)
print("1")
print("300000 100000000")
lst = list(range(1, 100000000, 100000000//310000))
random.shuffle(lst)
lst = lst[:300000]
assert len(lst) == 300000
print(*lst)
print(" ".join(["R", "L"]*((300000//2))))