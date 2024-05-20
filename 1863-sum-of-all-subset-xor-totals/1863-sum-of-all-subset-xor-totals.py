class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #bit manipulation
        n = len(nums)
        nth_bit = 1 << n
        total = 0

        for i in range(2**n):
            bit = bin(i | nth_bit)[3:] 
            temp = 0

            for j in range(n):
                if int(bit[j]):
                    temp ^= nums[j]
                    
            total += temp
            
        return total