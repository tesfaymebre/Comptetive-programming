class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0]*(len(s)+1)
        
        for start,end,direction in shifts:
            if direction:
                prefix_sum[start] += 1
                prefix_sum[end+1] -= 1
            else:
                prefix_sum[start] -= 1
                prefix_sum[end+1] += 1
                
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
                
        result = ['']*len(s)
        for j in range(len(s)):
            result[j] = chr((ord(s[j]) - ord('a') + prefix_sum[j])%26 + ord('a'))
            
        return ''.join(result)