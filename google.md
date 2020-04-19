# Google Coding Competitions

This refers to the [Kickstart](https://codingcompetitions.withgoogle.com/kickstart)and [Codejam](https://codingcompetitions.withgoogle.com/codejam)

Python 3 environment (but for some reason I need to install packages)

```
str_in = input()

def solve(w,h,l,u,r,d):
    # w,h destination
    #   l r  hole
    # u ###
    #   ###
    # d ### 

    res = 0
    # 6,4,1,3,3,4
    if u-2 >= 0 and w > r:
        # binom.cdf(1, 4, 0.5) # 1 = u-2 = 3-2, 4 = r+u-2 = 3+3-2
        res += binom.cdf(u-2, r+u-2, 0.5)
    if l-2 >= 0 and h > d:
        res += binom.cdf(l-2, d+l-2, 0.5)
    
    return res

for case in range(int(str_in)):
    strr = input()
    w,h,l,u,r,d = [int(x) for x in strr.split()]
    prob = solve(w,h,l,u,r,d)
    
    print("Case #{}: {}".format(case + 1, prob))


```



Libraries allowed in Google coding environment, other than native libraries

```
numpy
scipy
```

