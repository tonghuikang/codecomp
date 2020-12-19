# https://www.reddit.com/r/adventofcode/comments/kg1mro/2020_day_19_solutions/ggcohaa
import sys, re
table, strings = sys.stdin.read().split("\n\n")
T = dict(re.findall("(\d+):(.+)", table))

print(T)

# Special rules for part 2
T["8"] = "42+"
T["11"] = "|".join("42 " * i + "31 " * i for i in range(1, 10))

while len(T) > 1:
    # Find a "completed" rule to substitute
    k, v = next((k, v) for k, v in T.items() if not re.search("\d", v))
    T = { k1: re.sub(rf"\b{k}\b", f"({v})", v1)
          for k1, v1 in T.items() if k1 != k }

# Trim " and spaces, and add being/end markers.
reg = re.compile("^" + re.sub('[ "]', "", T["0"]) + "$")

print(reg)

print(sum(bool(reg.match(line)) for line in strings.split()))