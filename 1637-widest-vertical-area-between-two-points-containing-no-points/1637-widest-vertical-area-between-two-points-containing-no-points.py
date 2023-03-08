class Solution:
    # def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    #     points.sort()
    #     return max([points[i+1][0] - points[i][0] for i in range(len(points) - 1)])
    
    def maxWidthOfVerticalArea(self, points):
        A = sorted({x for x, y in points})
        return max([b - a for a, b in zip(A, A[1:])] + [0])