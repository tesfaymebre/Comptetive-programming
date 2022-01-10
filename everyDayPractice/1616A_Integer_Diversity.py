from collections import Counter
t = int(input())
max_num = []
for i in range(t):
    n = int(input())
    nums = Counter(list(map(int,input().split())))
    max_diff = 0
    for x in nums:
        if nums[x] > 1 and x != 0 and -1*x not in nums:
            max_diff += 2
        else:
            max_diff += 1
    max_num.append(max_diff)
print(*max_num,sep="\n")
