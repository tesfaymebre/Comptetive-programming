class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def winner(arr, k , index):

            if len(arr) == 1:
                return arr[0]

            index = index + k - 1

            while index >= len(arr):
                index = index - len(arr)

            arr.pop(index)

            return winner(arr,k,index)
        
        arr = []
        
        for i in range(n):
            arr.append(i+1)
        
        return winner(arr,k,0)
    
        