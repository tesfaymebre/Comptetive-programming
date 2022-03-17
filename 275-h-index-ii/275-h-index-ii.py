class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = citations[-1]
        h_indx = 0 if citations[-1] == 0 else 1
        while left <= right:
            mid = left + (right - left)//2
            if 0 <= n - mid < n and citations[n - mid] >= mid:
                h_indx = mid
                left = mid + 1
            else:
                right = mid - 1
        return h_indx 