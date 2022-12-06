class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        p1,p2 = 0, 1
        count = 1
        flag = 1 if p2 < len(arr) and arr[0] > arr[1] else 0

        while p2 < len(arr):
            if arr[p2-1] > arr[p2] and flag == 1:
                count = max(count,p2-p1+1)
                p2 += 1
                flag = 0
            elif arr[p2-1] < arr[p2] and flag == 0:
                count = max(count, p2-p1+1)
                p2 += 1
                flag = 1
            else:
                if arr[p2-1] == arr[p2]:
                    p2 += 1
                    p1 = p2 -1
                else:
                    p1 = p2 - 1

                flag = 1 if p2 < len(arr) and arr[p2-1] > arr[p2] else 0

        return count
    
    