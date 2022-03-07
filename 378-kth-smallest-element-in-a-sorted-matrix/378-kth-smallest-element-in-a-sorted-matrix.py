class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        n = len(matrix)
        
        if n*n / 2 < k:
        #construct minimum heap in order to 
        # return n^2 - k + 1 largest element
            for i in range(n):
                
                for j in range(n):
                    
                    if len(heap) < n*n - k + 1:
                        heappush(heap, matrix[i][j])
                    elif heap[0] < matrix[i][j]:
                        heapreplace(heap,matrix[i][j])
            return heap[0]
        
        else:
            #construct maximum heap in order to return kth smallest element
            for i in range(n):
                
                for j in range(n):
                    
                    if len(heap) < k:
                        heappush(heap, -matrix[i][j])
                    elif -heap[0] > matrix[i][j]:
                        heapreplace(heap, -matrix[i][j])
            
            return -heap[0]