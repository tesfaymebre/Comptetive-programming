class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #using bit manupulation
        xor = 0
        i = 1
        for num in nums:
            xor ^= num ^ i
            i += 1
               
        last_on_bit = xor&(xor-1) ^ xor
        num1 = 0
        
        for num in nums:
            if num & last_on_bit:
                num1 ^= num
                
        for i in range(1,len(nums)+1):
            if i & last_on_bit:
                num1 ^= i
                
        flag = False
        for num in nums:
            if num1 == num:
                flag = True
                break
                
        if flag:
            return [num1,num1^xor]
        else:
            return [num1^xor,num1]
       
        
        """
        items = Counter(nums)
        for i in range(1,len(nums)+1):
            if items[i] == 0:
                return [(items.most_common(1))[0][0] , i]
        """