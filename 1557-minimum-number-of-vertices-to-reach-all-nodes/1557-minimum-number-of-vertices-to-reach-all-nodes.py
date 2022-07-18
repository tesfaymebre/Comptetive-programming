class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        out_going = set(i for i in range(n))
        
        for v in edges:
            if v[1] in out_going:
                out_going.remove(v[1])
        
        return list(out_going)