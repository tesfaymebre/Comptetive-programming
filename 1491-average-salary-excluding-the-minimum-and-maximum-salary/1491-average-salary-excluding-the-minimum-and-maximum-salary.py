class Solution:
    def average(self, salary: List[int]) -> float:
        minn = min(salary)
        maxx = max(salary)
        
        return (sum(salary) - minn - maxx)/(len(salary)-2)