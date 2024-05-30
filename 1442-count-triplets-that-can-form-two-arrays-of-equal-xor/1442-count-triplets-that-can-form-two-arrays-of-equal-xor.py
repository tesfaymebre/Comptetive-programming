class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0]
        
        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
            
        ans = 0
        
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                for k in range(j,len(arr)):
                    if prefix_xor[j] ^ prefix_xor[i] == prefix_xor[k+1] ^ prefix_xor[j]:
                        ans += 1
                        
        return ans