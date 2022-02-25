class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 0:
            return -1
            
        total = 0
        que = deque()
        min_len = len(nums) + 1

        for val in enumerate(nums):

            while que and val[1] <= 0:
                ptr = que.pop()
                val = (ptr[0], ptr[1] + val[1])
                total -= ptr[1]

            if val[1] <= 0:
                total = 0
                que.clear()
            else:
                total += val[1]
                que.append(val)

                while total >= k:
                    ptr = que.popleft()
                    min_len = min(min_len, val[0] + 1 - ptr[0])
                    total -= ptr[1]
                    
        return min_len if min_len <= len(nums) else -1
                    
                
            
            