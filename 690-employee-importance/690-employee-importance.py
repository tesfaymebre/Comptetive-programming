"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def dfs(emp_id):
            self.total += employ[emp_id].importance
            for sub_id in employ[emp_id].subordinates:
                dfs(sub_id)
            return
                
        employ = dict()
        for em in employees:
            employ[em.id] = em
                
        self.total = 0     
        dfs(id) 
        
        return self.total
            