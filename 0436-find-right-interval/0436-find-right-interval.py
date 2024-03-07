class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        def helper(end):
            left = 0
            right = len(intervals) - 1
            best = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if intervals[mid][0] >= end:
                    right = mid - 1
                    best = mid
                else:
                    left = mid + 1
              
            return -1 if best == -1 else intervals[best][2]
        
        intervals = [[start,end,idx] for idx,(start,end) in enumerate(intervals)]
        
        result = [-1]*len(intervals)
        intervals.sort()
        
        for i in range(len(intervals)):
            index = helper(intervals[i][1])
            
            if index != -1:
                result[intervals[i][2]] = index
                
        return result