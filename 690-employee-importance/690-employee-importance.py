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
        indx = 0

        for i in range(len(employees)):
            if employees[i].id == id:
                indx = i
                break
        
        self.total = employees[indx].importance
        
        def dfs(sub_id):
            for sub in sub_id:
                for j in range(len(employees)):
                    if employees[j].id == sub:
                        self.total += employees[j].importance
                        dfs(employees[j].subordinates)

        dfs(employees[indx].subordinates)
        return self.total
                