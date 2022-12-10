class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_count = 0
        
        for num in nums:
            if num-1 not in nums:
                curr = num
                curr_count = 1
                
                while curr+1 in nums:
                    curr_count += 1
                    curr += 1
                    
                longest_count = max(longest_count,curr_count)
                
        return longest_count