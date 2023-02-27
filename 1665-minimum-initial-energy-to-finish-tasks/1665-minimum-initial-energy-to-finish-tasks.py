class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse = True)
        curr_total = 0
        res = 0
        
        for actual, minimum in tasks:
            if curr_total < minimum:
                res += minimum - curr_total
                curr_total = minimum - actual
            else:
                curr_total -= actual
            
        return res