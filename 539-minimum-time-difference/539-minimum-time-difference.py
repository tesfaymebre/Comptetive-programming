class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        zipped = zip(timePoints,timePoints[1:] + timePoints)
        zipped = list(zipped)
        min_diff = float('inf')
        
        def diff(x,y):
            return abs(int(x[:2])*60 + int(x[3:]) - (int(y[:2])*60 + int(y[3:])))
        
        for x,y in zipped:    
            min_diff = min(min_diff, diff(x,y))
        
        timePoints[0] = str(int(timePoints[0][:2]) + 24) + timePoints[0][2:]
        return min(min_diff, diff(timePoints[0],timePoints[-1]))
        
            
                                          
            
         