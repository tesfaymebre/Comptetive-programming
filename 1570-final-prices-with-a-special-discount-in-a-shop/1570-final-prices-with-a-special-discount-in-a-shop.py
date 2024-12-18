class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]
        stack = []

        for idx, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                answer[stack[-1]] = prices[stack[-1]] - price 
                stack.pop()

            stack.append(idx)

        return answer