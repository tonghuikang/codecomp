import sys
lst = list(map(int,input().split()))
 
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