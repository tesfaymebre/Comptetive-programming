class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        items = Counter(nums)

        for i in range(1,len(nums)+1):
            if items[i] == 0:
                return [(items.most_common(1))[0][0] , i]
