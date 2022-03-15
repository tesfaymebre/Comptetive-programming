class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        flip = 0
        count = 1
        c = 1
        d = 1
        
        for i in range(len(arr)-1):
            if flip == 0:
                if arr[i] < arr[i + 1]:
                    c += 1
                    count = max(count,d)
                    d = 1
                elif arr[i] > arr[i + 1]:
                    d += 1
                    count = max(count,c)
                    c = 1
                else:
                    count = max(count,c,d)
                    d = 1
                    c = 1
                flip = 1
            else:
                if arr[i] > arr[i + 1]:
                    c += 1
                    count = max(count,d)
                    d = 1
                elif arr[i] < arr[i + 1]:
                    d += 1
                    count = max(count,c)
                    c = 1
                else:
                    count = max(count,c,d)
                    d = 1
                    c = 1
                flip = 0
                
        count = max(count,c,d)
        return count
