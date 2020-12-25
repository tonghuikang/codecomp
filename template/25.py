x = 7
M = 20201227
for i in range(2,20201227+1):
    x = (7*x) % 20201227
    
    if x == 5764801:
        print(i)
    if x == 17807724:
        print(i)
    if x == 9789649:
        print(9789649, i)
        a = i
    if x == 3647239:
        print(3647239, i)
        
print(pow(3647239, a, 20201227))