class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        nums.sort()
        
        for i in range(len(nums)):
            p1 = i + 1
            p2 = len(nums) - 1
            
            while nums[i] not in seen and p1 < p2:
                if (nums[p1],nums[p2]) not in seen and nums[i] + nums[p1] + nums[p2] == 0:
                    ans.append([nums[i],nums[p1],nums[p2]])
                    seen.add((nums[p1],nums[p2]))
                    p1 += 1
                    p2 -= 1
                elif nums[i] + nums[p1] + nums[p2] > 0:
                    p2 -= 1
                else:
                    p1 += 1
            seen.add(nums[i])
            
        return ans
                