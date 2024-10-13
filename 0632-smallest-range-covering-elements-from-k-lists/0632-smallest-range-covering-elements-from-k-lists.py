class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        small = []
        n = len(nums)
        for i in range(n):
            heappush(small, (nums[i][0], i))

        large = max(small[i][0] for i in range(n))
        diff = large - small[0][0]
        ret = [small[0][0], large]

        while True:
            num, pos = heappop(small)
            nums[pos].pop(0)

            if len(nums[pos]) == 0:
                break
            if diff == 0:
                break

            new = nums[pos][0]
            heappush(small, (new, pos))
            large = max(large, new)
            if large - small[0][0] < diff:
                ret = [small[0][0], large]
                diff = large - small[0][0]
                
        return ret