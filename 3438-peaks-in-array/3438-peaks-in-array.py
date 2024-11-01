class SegmentTree:
    def __init__(self,nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (2*self.n)

        self.build()

    def isPeak(self,i):
        return self.nums[i-1] < self.nums[i] and self.nums[i] > self.nums[i+1]

    def build(self):
        for i in range(1,self.n-1):
            if self.isPeak(i):
                self.tree[i + self.n] = 1

        for j in range(self.n - 1, 0, -1):
            self.tree[j] = self.tree[j << 1] + self.tree[j << 1 | 1]

    def update_helper(self, index):
        index += self.n
        
        while index > 1:
            self.tree[index >> 1] = self.tree[index] + self.tree[index ^ 1]
            index >>= 1

    def update(self,index,val):
        self.nums[index] = val

        for i in range(max(1,index - 1),min(index + 2, self.n - 1)):
            if self.isPeak(i) and not self.tree[i + self.n]:
                self.tree[i + self.n] = 1
                self.update_helper(i)
            elif not self.isPeak(i) and self.tree[i + self.n]:
                self.tree[i + self.n] = 0
                self.update_helper(i)

    def query(self, left, right):
        left += self.n + 1
        right += self.n
        range_sum = 0

        while left < right:
            if left & 1:
                range_sum += self.tree[left]
                left += 1

            if right & 1:
                right -= 1
                range_sum += self.tree[right]

            left >>= 1
            right >>= 1

        return range_sum

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        segmentTree = SegmentTree(nums)

        res = []

        for x in queries:
            if x[0] == 1:
                res.append(segmentTree.query(x[1],x[2]))
            else:
                segmentTree.update(x[1],x[2])

        return res