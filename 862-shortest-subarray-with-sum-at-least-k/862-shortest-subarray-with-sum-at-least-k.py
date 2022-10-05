class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que = deque([[0,0]])
        cur_sum = 0
        ans = len(nums) + 1
        
        for i in range(len(nums)):
            cur_sum += nums[i]
            
            while que and cur_sum - que[0][1] >= k:
                ans = min(ans,i - que.popleft()[0] + 1)
                
            while que and que[-1][1] > cur_sum:
                que.pop()
                
            que.append([i+1,cur_sum])
            
        return ans if ans != len(nums) + 1 else -1