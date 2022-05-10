class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        diff = abs(len(version1) - len(version2)) + 1
        zeros = ['0']*diff
        zipped = zip(v1 + zeros, v2 + zeros)
        zipped = list(zipped)
        
        for i in range(len(zipped)):
            if int(zipped[i][0]) > int(zipped[i][1]):
                return 1
            elif int(zipped[i][0]) < int(zipped[i][1]):
                return -1
        return 0
        
        
        