class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda a:a[0])
        merged = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] <= end:
                if intervals[i][1] >= end:
                    end = intervals[i][1]
            else:
                merged.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
        merged.append([start,end])
        return merged
                    
