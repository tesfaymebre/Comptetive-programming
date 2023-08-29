class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cur_penalty = min_penalty = 0
        earliest_hour = 0
        
        for i, ch in enumerate(customers):
            if ch == 'Y':
                cur_penalty -= 1
            else:
                cur_penalty += 1

            if cur_penalty < min_penalty:
                earliest_hour = i + 1
                min_penalty = cur_penalty
                
        return earliest_hour