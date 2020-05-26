# Speed optimisation

Is there really a case where the code passes on C++ but not Python?



When you are nesting for loops but intend to run on O(n), avoid enumerate for the inner loop.

Replacing 

```python
          for z,x in enumerate(lst[i+1:], start=i+1):
```

with

```python
          for z in range(i+1, n_months+1):
```

would have made my code run within time limit. I am still trying to find a reproducible example.

