class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        
        if total % k:
            return False
        
        subset_sum = total // k
        subsets = [0] * k
        nums.sort(reverse=True)
        
        def back_t(idx):
            if idx == len(nums):
                for i in range(k):
                    if subsets[i] != subset_sum:
                        return False
                    
                return True
            
            for j in range(k):
                if subsets[j] + nums[idx] <= subset_sum:
                    subsets[j] += nums[idx]
                    
                    if back_t(idx + 1):
                        return True
                    
                    subsets[j] -= nums[idx]
                    
                    if subsets[j] == 0:
                        break
                    
            return False
        
        return back_t(0)
                