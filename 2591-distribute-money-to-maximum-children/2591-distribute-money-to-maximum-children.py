class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children > money:
            return -1
        
        count = 0
        
        while children and money - 8 >= children - 1:
            money -= 8
            children -= 1
            count += 1
            
        if children == 1 and money == 4:
            return count - 1
        elif children == 0 and money > 0:
            return count - 1
        
        return count