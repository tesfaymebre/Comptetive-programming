class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        for idx,cost in enumerate(costs):
            coins -= cost 
            
            if coins < 0:
                return idx
            
        return len(costs)
            