class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = sum([1 for i in range(len(heights)) if heights[i] != expected[i]])
        return count
        
