from itertools import combinations
N = int(input())
low_letter = input().split()
K = int(input())
out = tuple(combinations(low_letter,K))
count=0

for comb in out:
    if 'a' in comb:
        count+=1

print(round((count/len(out)),3))
