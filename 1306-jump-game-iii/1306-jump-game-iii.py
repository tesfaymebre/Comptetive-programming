class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        visited = set()
        in_bound = lambda indx: 0 <= indx < len(arr)
        
        queue.append(start)
        visited.add(start)
        
        while queue:
            n = len(queue)
            for j in range(n):
                i = queue.popleft()
                if arr[i] == 0:
                    return True

                right_indx = i + arr[i]
                if in_bound(right_indx) and right_indx not in visited:
                    queue.append(right_indx)
                    visited.add(right_indx)

                left_indx = i - arr[i]
                if in_bound(left_indx) and left_indx not in visited:
                    queue.append(left_indx)
                    visited.add(left_indx)
                    
        return False
        
        