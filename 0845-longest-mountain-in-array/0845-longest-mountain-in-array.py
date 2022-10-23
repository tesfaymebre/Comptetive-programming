class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        size = len(arr)
        ans = 0
        base = 0
        
        while base < size:
            end = base
            if end+1 < size and arr[end] < arr[end+1]:
                
                while end + 1 < size and arr[end] < arr[end+1]:
                    end += 1
                    
                if end+1 < size and arr[end] > arr[end+1]:
                    
                    while end+1 < size and arr[end] > arr[end+1]:
                        end += 1
                        
                    ans = max(ans,end-base+1)
                    
            base = max(end,base + 1)
            
        return ans