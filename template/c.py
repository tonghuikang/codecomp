X,Y,Z = 3,5,7

import math

def calc(X,Y,Z):
    if Y*math.log(X) < 10*math.log(10):
        res = ("{:.4f}".format((X**Y)/Z))[:-1]
        if len(res) > 7:
            res = res[-7:]
        return res 
    return "{:.4f}".format(pow(X, Y, Z*1000)/Z)[-9:-1].zfill(7)

print(calc(3,5,7))
print(calc(4,7,32))
print(calc(3,2,36))
print(calc(7,4,47))
print(calc(13,6,479))
print(calc(1234,56789,123456))
print(calc(999999999,128,1000000))