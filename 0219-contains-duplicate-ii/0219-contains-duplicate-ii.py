class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        group = defaultdict(int)
        
        for index,num in enumerate(nums):
            if num in group and abs(group[num] - index) <= k:
                return True
            
            group[num] = index
            
        return False