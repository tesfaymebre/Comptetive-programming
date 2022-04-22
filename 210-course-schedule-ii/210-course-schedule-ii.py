class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        out_going = defaultdict(set)
        
        for des, src in prerequisites:
            in_degrees[des] += 1
            out_going[src].add(des)
        
        queue = deque()
        
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                queue.append(i)
        
        order = []
        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            
            for des in out_going[curr]:
                in_degrees[des] -= 1
                
                if in_degrees[des] == 0:
                    queue.append(des)
        return order if numCourses == len(order) else []