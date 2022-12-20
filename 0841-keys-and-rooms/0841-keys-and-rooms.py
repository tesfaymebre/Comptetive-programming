class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque()
        seen = set()
        
        for key in rooms[0]:
            queue.append(key)
            
        seen.add(0)
        
        while queue:
            temp = queue.popleft()
            seen.add(temp)
            
            for key in rooms[temp]:
                if key not in seen:
                    queue.append(key)
                
        return len(seen) == len(rooms)