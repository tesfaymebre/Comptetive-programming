class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = defaultdict(int)
        ans = []
        j = 10
        
        def getMask(seq):
            mask = [0,0,0,0]
            
            for i in range(len(seq)):
                if seq[i] == 'A':
                    mask[0] |= (1<<i)
                if seq[i] == 'C':
                    mask[1] |= (1<<i)
                if seq[i] == 'T':
                    mask[2]  |= (1<<i)
                if seq[i] == 'G':
                    mask[3] |= (1<<i)
                    
            #print(mask)
            return tuple(mask)

        for i in range(len(s)):
            if j <= len(s):
                temp = s[i:i+j]
                mask = getMask(temp)
                
                if seen[mask] == 1:
                    ans.append(temp)
                
                seen[mask] += 1
            
        return ans
                