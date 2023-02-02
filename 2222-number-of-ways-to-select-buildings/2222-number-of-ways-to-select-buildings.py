class Solution:
    def numberOfWays(self, s: str) -> int:
        size = len(s)
        prefix_zeros = [0]*(size + 1)
        prefix_ones = [0]*(size + 1)
        
        for i in range(len(s)):
            if s[i] == '0':
                prefix_zeros[i+1] = prefix_zeros[i] + 1
                prefix_ones[i+1] = prefix_ones[i]
            else:
                prefix_ones[i+1] = prefix_ones[i] + 1
                prefix_zeros[i+1] = prefix_zeros[i]
                
        valid_ways = 0
        
        for j in range(1,len(s)-1):
            if s[j] == '0':
                left_side = prefix_ones[j]
                right_side = prefix_ones[-1] - prefix_ones[j+1]
                valid_ways += left_side*right_side
            else:
                left_side = prefix_zeros[j]
                right_side = prefix_zeros[-1] - prefix_zeros[j+1]
                valid_ways += left_side*right_side
                    
        return valid_ways
            
        