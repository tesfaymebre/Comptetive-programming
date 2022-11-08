class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
            
        last_on_bit = xor&(xor-1) ^ xor
        num1 = 0
        
        for num in nums:
            if num & last_on_bit:
                num1 ^= num
                
        num2 = xor^num1
        return [num1,num2]