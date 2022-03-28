class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = defaultdict(int)
        ans = []
        j = 10
        
        for i in range(len(s)):
            if j <= len(s):
                temp = s[i:i+j]
                if seen[temp] == 1:
                    ans.append(temp)
                    
                seen[temp] += 1
            
        return ans
                