class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.size = len(self.w)
        self.prefix_sum = [0]
        
        for val in self.w:
            self.prefix_sum.append(self.prefix_sum[-1]+val)

    def pickIndex(self) -> int:
        rand_num = random.randint(1,self.prefix_sum[-1])
        return bisect.bisect_left(self.prefix_sum,rand_num) - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()