class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        dots = '.'*n
        
        def backT(row,path,backSlash,froSlash,v):
            if row >= n:
                res.append(path[:])
                return
            
            for col in range(n):
                if (row - col) in backSlash or (row + col) in froSlash or col in v:
                    continue
                    
                backSlash.add((row - col))
                froSlash.add(row+col)
                v.add(col)
                
                backT(row+1,path + [dots[:col]+'Q' + dots[col+1:]],backSlash,froSlash,v)
                backSlash.remove((row - col))
                froSlash.remove(row+col)
                v.remove(col)
            
        backT(0,[],set(),set(),set())
        return res        