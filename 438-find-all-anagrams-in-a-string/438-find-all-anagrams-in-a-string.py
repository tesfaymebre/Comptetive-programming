class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        myDictP = Counter(p)
        myDictS = Counter(s[:len(p)])
        ans = []
        
        p1,p2 = 0,len(p)
        
        while p2 <= len(s):
            if myDictP == myDictS:
                ans.append(p1)
            
            myDictS[s[p1]] -= 1
            if myDictS[s[p1]] <= 0:
                myDictS.pop(s[p1])
                
            if p2 < len(s):
                myDictS[s[p2]] += 1
                
            p2 += 1
            p1 += 1
            
        return ans
                
            
                    