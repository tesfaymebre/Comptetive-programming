from collections import Counter
num_shoes = int(input())
shoeSize = Counter(input().split())
n_cust = int(input())
earned = 0
for i in range(n_cust):
    desired = input().split()
    if shoeSize[desired[0]] != 0:
        shoeSize[desired[0]]-= 1
        earned += int(desired[1])
print(earned)
