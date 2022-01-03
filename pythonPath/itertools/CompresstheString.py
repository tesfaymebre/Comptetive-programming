from itertools import groupby
s = input()
groups = []
for x,c in groupby(s):
    print("(",len(list(c)),", ",x,")",end=" ",sep = "")
