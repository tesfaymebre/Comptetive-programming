class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        items = OrderedDict()
        for i in range(len(s)):
            if (s[i] not in items):
                if (t[i] not in items.values()):
                    items[s[i]] = t[i]
                else:
                    return False
            elif items[s[i]] != t[i]:
                return False
        return True
