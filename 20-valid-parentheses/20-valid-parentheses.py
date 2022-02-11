class Solution:
    def isValid(self, s: str) -> bool:
        li = {"(":")","{":"}","[":"]"}
        li2 = []
        for x in s:
            if x in li:
                li2.append(li[x])
            elif len(li2) > 0 :
                val = li2.pop()
                if val != x:
                    return False
            else:
                return False
            
        if len(li2)==0:        
            return True
            