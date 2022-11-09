class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        result = set()
                
        for i in range(2**n):
            temp = []
            for j in range(n-1,-1,-1):
                pos = i & 1<<j
                
                if i & 1<<j and s[-j-1].isalpha():
                        temp.append(s[-j-1].upper())
                elif s[-j-1].isalpha():
                    temp.append(s[-j-1].lower())
                else:
                    temp.append(s[-j-1])
                        
            result.add(''.join(temp))
            
        return list(result)
        