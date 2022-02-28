class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        diction = {}
        
        for vals in edges:
            if vals[0] not in diction:
                diction[vals[0]] = 0
                
            if vals[1] not in diction:
                diction[vals[1]] = 0
                
            diction[vals[0]] += 1
            diction[vals[1]] += 1
        
        for key in diction.keys():
            if diction[key] == len(edges):
                return key
                
                