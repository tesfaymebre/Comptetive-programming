class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        
        arr = [-1] * n
        record = dict()
        
        for i in range(n - 1, -1, -1):
            if nums[i] in record:
                arr[i] = record[nums[i]]
                
            record[nums[i]] = i

        left = 0
        seen = set()
        
        for right in range(n):
            seen.add(nums[right])
            
            while len(seen) > k:
                if arr[left] == -1 or arr[left] > right:
                    seen.remove(nums[left])
                    
                left += 1
                
            if len(seen) == k:
                count = left
                
                while arr[count] != -1 and arr[count] <= right:
                    count += 1
                    
                ans += count - left + 1
                
        return ans