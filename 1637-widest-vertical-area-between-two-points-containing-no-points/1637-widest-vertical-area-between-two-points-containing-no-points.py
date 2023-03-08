class Solution:
    # def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    #     A = sorted([x for x, y in points])
    #     return max([A[i+1] - A[i] for i in range(len(points) - 1)])
    
    def maxWidthOfVerticalArea(self, points):
        A = sorted({x for x, y in points})
        return max([b - a for a, b in zip(A, A[1:])] + [0])