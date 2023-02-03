class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.size = len(self.w)
        self.prefix_sum = [0]
        
        for val in self.w:
            self.prefix_sum.append(self.prefix_sum[-1]+val)
            
    def binarySearch(self,target):
        left = 0
        right = self.size - 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return left
        
    def pickIndex(self) -> int:
        rand_num = random.randint(1,self.prefix_sum[-1])
        
        return self.binarySearch(rand_num) - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()