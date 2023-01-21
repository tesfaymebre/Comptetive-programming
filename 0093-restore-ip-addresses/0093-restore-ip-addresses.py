class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(s, start, buckets, res):
            if len(buckets) == 4:
                if start == len(s):
                    res.append(".".join(buckets))
                return 
            if len(buckets) > 4:
                return 
            for i in range(1, 4):
                if start + i > len(s):
                    break
                if i > 1 and s[start] == "0":
                    continue
                if int(s[start:start+i]) > 255:
                    continue
                backtrack(s, start+i, buckets + [s[start:start+i]], res)
                
        res = []
        backtrack(s, 0, [], res)
        return res