class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        prefix_xor = [0]
        
        for num in arr:
            prefix_xor.append(prefix_xor[-1] ^ num)
            
        ans = 0
        
        for i in range(len(arr)):
            for k in range(i + 1,len(arr)):
                if prefix_xor[k + 1] == prefix_xor[i]:
                    ans += k - i
        return ans