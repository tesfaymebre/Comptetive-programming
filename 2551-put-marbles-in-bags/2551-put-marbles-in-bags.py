class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        pair_weights = []
        
        for i in range(len(weights)-1):
            pair_weights.append(weights[i] + weights[i+1])
            
        pair_weights.sort()
        
        ans = 0
        for j in range(k-1):
            ans += pair_weights[-(j+1)] - pair_weights[j]
            
        return ans