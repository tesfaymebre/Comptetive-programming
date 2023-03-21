class Solution:
    def nextGreaterElement(self, n: int) -> int:
        arr = list(str(n))
        
        for i in range(len(arr)-1,0,-1):
            if arr[i] > arr[i-1]:
                greater = [i,arr[i]]
                
                for j in range(i+1,len(arr)):
                    if arr[j] > arr[i-1] and greater[1] > arr[j]:
                        greater = [j,arr[j]]
                        
                arr[greater[0]],arr[i-1] = arr[i-1],arr[greater[0]]
                
                temp = sorted(arr[i:])
                arr[i:] = temp[:]
                ans = int(''.join(arr))
                
                if ans <= 2147483647:
                    return ans
                else:
                    return -1
            
        return -1