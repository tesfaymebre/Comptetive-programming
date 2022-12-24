class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        left = 0
        right = len(arr)-1
        
        while left < right:
            if arr[left] == 0:
                right -= 1
                
            left += 1
        
        pos = len(arr)-1
        
        if right - left == 0:
            arr[-1] = arr[left]
            left -= 1
            pos -= 1
        else:
            left -= 1
        
        while pos > -1:
            if arr[left] == 0:
                arr[pos] = 0
                arr[pos-1] = 0
                pos -= 2
            else:
                arr[pos] = arr[left]
                pos -= 1
                
            left -= 1
                