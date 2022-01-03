from itertools import combinations
s = input().split()
s_sorted = sorted(tuple(s[0]))

for i in range(1,int(s[1])+1):
    out = tuple(combinations(s_sorted,i))
    for x in out:
        print("".join(x))
