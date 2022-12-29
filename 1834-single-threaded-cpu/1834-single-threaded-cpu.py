class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:    
        sorted_tasks = []
        
        for i,task in enumerate(tasks):
            sorted_tasks.append(task+[i])
            
        sorted_tasks.sort()
        
        heap = []
        result = []
        time = 0
        task_idx = 0
        
        while task_idx < len(sorted_tasks) or heap:
            if not heap:
                time = max(time,sorted_tasks[task_idx][0])
                
            while task_idx < len(sorted_tasks) and time >= sorted_tasks[task_idx][0]:
                _, process_time, original_idx = sorted_tasks[task_idx]
                heapq.heappush(heap,(process_time,original_idx))
                task_idx += 1
            
            processing_time,curr_idx = heapq.heappop(heap)
            result.append(curr_idx)
            time += processing_time
        
        return result