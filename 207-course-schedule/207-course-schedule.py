class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = [0] * numCourses
        out_going = defaultdict(set)
        
        for des, src in prerequisites:
            in_degrees[des] += 1
            out_going[src].add(des)
        
        queue = deque()
        
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                queue.append(i)
                
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            
            for des in out_going[curr]:
                in_degrees[des] -= 1
                
                if in_degrees[des] == 0:
                    queue.append(des)
        
        return count == numCourses