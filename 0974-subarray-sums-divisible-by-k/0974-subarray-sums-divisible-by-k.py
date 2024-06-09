class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mods = defaultdict(int)
        mods[0] = 1
        running_sum = 0
        count = 0
        
        for num in nums:
            running_sum += num
            remain = running_sum % k
            
            count += mods[remain]
            mods[remain] += 1
            
        return count
        
        