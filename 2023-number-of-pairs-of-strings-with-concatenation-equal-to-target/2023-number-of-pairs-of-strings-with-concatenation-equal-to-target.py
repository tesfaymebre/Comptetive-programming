class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        seen = defaultdict(int)
        count = 0
        
        for num in nums:
            right_side = target[len(num):]
            left_side = target[:-len(num)]
            
            if num == target[:len(num)] and right_side in seen:
                count += seen[right_side]
                
            if num == target[-len(num):] and left_side in seen:
                count += seen[left_side]
            
            seen[num] += 1
            
        return count