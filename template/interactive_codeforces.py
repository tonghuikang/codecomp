import sys
k = int(input())

sus = []

for i in range(2**k-1):
    
    


print ("First",flush = True)
 
while True:
 
    Mmax = max(lst)
    Mmin = min(lst)
    Mmid = sum(lst) - Mmax - Mmin
 
    if Mmax - Mmid == Mmid - Mmin:
        print(Mmax - Mmid, flush = True)
        idx = int(input())
        if idx == 0:
            sys.exit()
        lst[idx-1] += Mmax - Mmid
 
    B = Mmax - Mmin
    A = Mmid - Mmin
 
    print(2*B - A, flush=True)
    idx = int(input())
    if idx == 0:
        sys.exit()
    lst[idx-1] += 2*B - A