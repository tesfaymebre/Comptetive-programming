class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]
        
        ans = []
        ptr1 = 0
        ptr2 = len(matrix)
        curr = 0
                
        while  matrix[curr]:
                
            if ptr1 == curr:
                
                while matrix[curr]:
                    ans.append(matrix[curr].pop(0))
                
                curr += 1
                ptr2 -= 1
                
                while ptr2 != curr and matrix[curr]:
                    ans.append(matrix[curr].pop())
                    curr += 1
                
            else:
              
                while matrix[curr]:
                    ans.append(matrix[curr].pop())
               
                curr -= 1
                ptr1 += 1
                
                while ptr1 != curr and matrix[curr]:
                    ans.append(matrix[curr].pop(0))
                    curr -= 1
                
        return ans
                