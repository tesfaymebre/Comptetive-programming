class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = []
        start = 0
        left = 0
        right = len(s)-1
        temp = 0
        
        while left < len(s):
            
            while right >= temp and s[right] != s[left]:
                right -= 1
                
            temp = max(temp,right)
            
            if left == temp:
                ans.append(temp - start + 1)
                start = left + 1
                
            left += 1
            right = len(s)-1
            
        return ans
        
        
        