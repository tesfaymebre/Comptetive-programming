class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:    
        sorted_tasks = []
        
        for i,task in enumerate(tasks):
            sorted_tasks.append(task+[i])
            
        sorted_tasks.sort()
        
        heap = []
        result = []
        time = 0
        idx = 0
        
        while idx < len(sorted_tasks):
            if not heap:
                time = max(time,sorted_tasks[idx][0])
                
            if sorted_tasks[idx][0] <= time:
                heapq.heappush(heap,(sorted_tasks[idx][1],sorted_tasks[idx][2]))
                idx += 1
                continue
              
            while heap and time < sorted_tasks[idx][0]:
                temp,i = heapq.heappop(heap)
                result.append(i)
                time += temp
            
        while heap:
            temp,idx = heapq.heappop(heap)
            result.append(idx)
            
        return result