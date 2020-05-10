# Coding platforms

### Codeforces
```python
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in range(n):
        a[i] = ((a[i]%n)+i)%n
    if(len(set(a)) == n):
        print("YES")
    else:
        print("NO")
```



### Leetcode
Pretty intuitive. Very regular contest. Problems are sufficiently novel every time. I want the T-shirt.

### Google Coding platforms

This refers to the [Kickstart ](https://codingcompetitions.withgoogle.com/kickstart)and [Codejam](https://codingcompetitions.withgoogle.com/codejam) environments. This may be applicable to other platform. You do not need this for Leetcode and their IDE is too good.



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



To run with an input file

```
python3 a.py < a.in
```



## Reading variables

Try this

```python
T, B = map(int, input().split())
```





## Printing

The output is read from std out. How can we avoid the process of commenting and uncommmenting the code?







## Interactive problems

You need to obtain `interactive_runner.py` which applies to all CodeJam problem post-2020, and `local_testing_tool.py` from the specific problem.

```bash
python interactive_runner.py python3 sample_local_testing_tool.py 2 -- python3 sample_interactive.py
```



For competition usage

```bash
python interactive_runner.py python3 local_testing_tool.py 2 -- python3 interactive.py
```



This is how to flush.

```python
T, B = map(int, input().split())
print('B:', B, file=sys.stderr)
for _ in range(T):
    array = QuantumArray(B)
    print('guess:', ''.join(array.bits), file=sys.stderr)
    print(''.join(array.bits), flush=True)
    if input() == 'N': sys.exit()
```





## Directions

```
    d = {}
    d["N"] = (1,0)
    d["S"] = (-1,0)
    d["E"] = (0,1)
    d["W"] = (0,-1)
    
    if coords[0] > 0:
        res += "N"*coords[0]
    else:
        res += "S"*abs(coords[0])

    if coords[1] > 0:
        res += "E"*coords[0]
    else:
        res += "W"*abs(coords[0])
```

