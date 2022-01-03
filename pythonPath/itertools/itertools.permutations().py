from itertools import permutations
s1 = input().split()
S = sorted(tuple(s1[0]))
out = tuple(permutations(S,int(s1[1])))
for i in range(len(out)):
    print("".join(out[i]))
