class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        inc = set()
        dec = set()
        
        queue = deque()
        
        for i in range(len(security)):
            if security[i] <= security[i-1]:
                queue.append(i)
            else:
                queue = deque()
                queue.append(i)
                
            if len(queue) == time + 1:
                dec.add((queue[0],queue[-1]))
                queue.popleft()
                
        queue = deque()
        
        for j in range(len(security)):
            if security[j] >= security[j-1]:
                queue.append(j)
            else:
                queue = deque()
                queue.append(j)
                
            if len(queue) == time + 1:
                inc.add((queue[0],queue[-1]))
                queue.popleft() 
                
        ans = []
        
        for k in range(time, len(security)):
            if (k - time, k) in dec and (k, k + time) in inc:
                ans.append(k)
        return ans