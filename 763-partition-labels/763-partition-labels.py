class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occurence = Counter(s)
        li = []
        ans = []
        ptr = 0
        ptr2 = 0
        start = 0
        
        while ptr < len(s):
            if ptr - start == 0:
                ch = s[ptr]
                occurence[ch] -= 1
                ptr += 1
            elif ptr2 < ptr and occurence[s[ptr2]] == 0:
                ptr2 += 1
            elif ptr2 >= ptr:
                ans.append(ptr - start)
                start = ptr2
            else:
                ch = s[ptr]
                ptr += 1
                occurence[ch] -= 1
                
        ans.append(ptr - start)
        return ans
                
            