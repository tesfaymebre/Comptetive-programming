class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints = [int(x[:2])*60 + int(x[3:]) for x in timePoints]
        timePoints.sort()
        min_diff = [timePoints[i]-timePoints[i-1] for i in range(1,len(timePoints))]
        min_diff.append(timePoints[0]+(24*60)-timePoints[len(timePoints)-1])
        return min(min_diff)
