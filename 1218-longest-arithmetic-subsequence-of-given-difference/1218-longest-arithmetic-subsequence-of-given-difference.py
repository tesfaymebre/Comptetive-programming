class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count = dict()
        length = 1
        
        for i in range(len(arr)):
            count[arr[i]] = count[arr[i]-difference] + 1 if (arr[i]-difference) in count else 1
            length = max(length,count[arr[i]])
        
        return length