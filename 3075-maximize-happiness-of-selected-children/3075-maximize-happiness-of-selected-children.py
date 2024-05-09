class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        minus = 0
        
        for i in range(k):
            happiness[i] = max(0, happiness[i] - minus)
            minus += 1
                      
        return sum(happiness[:k]) 