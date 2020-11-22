import sys

with open('e9', 'w') as f:
    sys.stdout = f 
    print(2000, 2000)
    print("S" + "."*1999)
    for i in range(1998):
        print("."*2000)
    print("."*1999 + "G")

with open('e8', 'w') as f:
    sys.stdout = f 
    print(2000, 2000)
    print("S" + "#" + "."*1998)
    for i in range(1998):
        print("."*2000)
    print("."*1999 + "G")