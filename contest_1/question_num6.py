nums = list(map(int,input().split()))
# nums = [0,1,0,3,12]
for j in range(len(nums)-1):
    for i in range(len(nums)-1):
        start = nums[i]
        if start == 0:
            temp = nums[i+1]
            nums[i+1] = start
            nums[i] = temp
print(nums)
