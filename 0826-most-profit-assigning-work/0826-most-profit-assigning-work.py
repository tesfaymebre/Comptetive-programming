class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_profit = list(zip(difficulty,profit))
        difficulty_profit.sort()
        worker.sort()
        
        ans = 0
        temp = 0
        left = 0
        
        for w in worker:
            while left < len(difficulty) and w >= difficulty_profit[left][0]:
                temp = max(temp,difficulty_profit[left][1])
                left += 1
                
            ans += temp
            
        return ans