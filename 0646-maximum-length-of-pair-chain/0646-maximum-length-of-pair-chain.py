class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        
        count = 1
        temp = pairs[0][1]
        
        for s,e in pairs:
            if temp < s:
                temp = e
                count += 1
                
        return count