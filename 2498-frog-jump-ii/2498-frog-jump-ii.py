class Solution:
    def maxJump(self, stones: List[int]) -> int:
        forward = stones[0]
        backward = stones[0]
        
        result = 0
        
        for i,dist in enumerate(stones):
            if i&1:
                result = max(result,abs(backward-dist))
                backward = dist
            else:
                result = max(result,abs(forward-dist))
                forward = dist
                
        return result