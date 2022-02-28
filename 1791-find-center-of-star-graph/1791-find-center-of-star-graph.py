class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        def def_value():
            return 0
        
        counting = defaultdict(def_value)
        
        for vals in edges:
          
            counting[vals[0]] += 1
            counting[vals[1]] += 1
            
            if counting[vals[0]] == len(edges):
                return vals[0]
            elif counting[vals[1]] == len(edges):
                return vals[1]
                
                