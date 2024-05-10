class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fractions = []
        
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                fractions.append((arr[i] / arr[j], i, j))
        
        fractions.sort()
        
        return [arr[fractions[k-1][1]], arr[fractions[k-1][2]]]