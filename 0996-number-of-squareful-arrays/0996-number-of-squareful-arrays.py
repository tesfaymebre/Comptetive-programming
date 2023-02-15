class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        self.count = 0
        n = len(nums)
        
        nums.sort()
        
        visited = [0] * n
        cur = []
        
        def dfs():
            if len(cur) == n:
                self.count += 1
                return
            
            prev = None
            if not cur:
                for i in range(n):
                    if nums[i] == prev:
                        continue
                        
                    prev = nums[i]
                    cur.append(nums[i])
                    visited[i] = 1
                    dfs()
                    cur.pop()
                    visited[i] = 0
                    
            else:
                for i in range(n):
                    if visited[i] == 1:
                        continue
                        
                    if nums[i] == prev:
                        continue
                        
                    prev = nums[i]
                    if int(sqrt(nums[i] + cur[-1]))**2 == nums[i] + cur[-1]:
                        cur.append(nums[i])
                        visited[i] = 1
                        dfs()
                        cur.pop()
                        visited[i] = 0
                        
            return
        
        dfs()
        
        return self.count