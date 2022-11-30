class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        #binary search solution
        def BS(h):
            left = 0
            right = len(accumulate)-1
            
            while left <= right:
                mid = left + (right-left)//2
                
                if accumulate[mid][1] < h:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return left
        
        envelopes.sort(key = lambda x: (x[0],-x[1]))
        accumulate = [envelopes[0]]
        
        for w,h in envelopes:
            pos = BS(h)
            
            if pos == len(accumulate) and accumulate[-1][0] < w:
                accumulate.append([w,h])
            else:
                accumulate[pos] = [w,h]
        
        return len(accumulate)
        