class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        
        for i in range(n):
            money += (i % 7) + (i//7) + 1
            
        return money