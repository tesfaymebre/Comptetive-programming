class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        arr = list(s)
        
        return ''.join(sorted(arr,key = lambda x: (-count[x],x)))