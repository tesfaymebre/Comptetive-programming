class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.tree = [0] * (2*self.n)
        self.build()

    def build(self):
        for i in range(self.n):
            self.tree[i + self.n] = self.nums[i]

        for j in range(self.n - 1, 0, -1):
            self.tree[j] = self.tree[j<<1] + self.tree[j<<1 | 1]

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val
        index += self.n
        self.tree[index] = val

        while index > 1:
            self.tree[index >> 1] = self.tree[index] + self.tree[index ^ 1]
            index >>= 1

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n + 1
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


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)