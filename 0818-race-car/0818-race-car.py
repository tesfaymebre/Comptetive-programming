class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        queue.append((0, 1, 0))
        
        while queue:
            pos, speed, n = queue.popleft()
            
            if pos == target:
                return n
            
            queue.append((pos+speed, speed*2, n+1))
            
            if speed > 0:
                if pos + speed > target:
                    queue.append((pos, -1, n+1))
            else:
                if pos + speed < target:
                    queue.append((pos, 1, n + 1))