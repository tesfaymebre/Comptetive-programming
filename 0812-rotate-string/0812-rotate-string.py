class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False 
            
        def LPS_preprocess(pattern):
            n = len(pattern)
            lps = [0]*n
            j = 0
            i = 1
            while i < n:
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
                    i += 1
                else:
                    if j == 0:
                        i += 1
                    else:
                        j = lps[j-1]
            return lps

        s += s
        n = len(s)
        m = len(goal)
        lps = LPS_preprocess(goal)
     
        i = 0
        j = 0
        while i < n:
            if s[i] == goal[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]

            if j == m:
                return True

        return False