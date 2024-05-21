class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # solution 2 top down dp
        total = sum(nums)
        
        if total % k:
            return False
        
        subset_sum = total // k
        nums.sort()
        
        def dp(visited, curr_total):
            if (visited, curr_total) not in memo:
                if visited == mask:
                    return True

                for i in range(len(nums)):
                    if (visited >> i) & 1:
                        continue

                    if nums[i] + curr_total > subset_sum:
                        break    

                    if nums[i] + curr_total == subset_sum:
                        if dp(visited | 1 << i, 0):
                            return True
                    elif dp(visited | 1 << i, nums[i] + curr_total):
                        return True

                memo[(visited, curr_total)] = False
            return memo[(visited, curr_total)]
        
        mask = (1 << len(nums)) - 1  # bit '1' is for visted. mask is set to indicate all nums are visited
        memo = {}
        return dp(0,0)
        
        """
        # solution 1 backtrack
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
        """
                