class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def helper(pos,amount):
            if (pos,amount) not in memo:
                if amount == 0:
                    return 1

                if pos == len(coins):
                    return 0

                pick = 0

                if amount >= coins[pos]:
                    pick += helper(pos,amount-coins[pos])

                not_pick = helper(pos+1,amount)

                memo[(pos,amount)] = pick + not_pick   
                
            return memo[(pos,amount)]
        
        memo = {}
        return helper(0,amount)