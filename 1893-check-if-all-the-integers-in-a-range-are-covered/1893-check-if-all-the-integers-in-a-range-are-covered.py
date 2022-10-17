class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        prefix_sum = [0]*52
        
        for st,end in ranges:
            prefix_sum[st] += 1
            prefix_sum[end+1] += -1
            
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i-1]
            
        for j in range(left,right+1):
            if prefix_sum[j] == 0:
                return False
            
        return True
        