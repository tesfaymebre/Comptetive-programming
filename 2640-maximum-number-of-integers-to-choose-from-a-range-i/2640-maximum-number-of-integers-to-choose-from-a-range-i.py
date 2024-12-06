class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curr_sum = 0
        count = 0

        for i in range(1,n+1):
            if i not in banned:
                curr_sum += i

                if curr_sum > maxSum:
                    return count

                count += 1
        
        return count