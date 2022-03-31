class Solution:
    def minimumOperations(self, nums: List[int]) -> int: 
        if len(nums) == 1:
            return 0
        
        odd = Counter(nums[1::2])
        even = Counter(nums[0::2])
        odd[0] = 0
        even[0] = 0
        
        max_even = max(even, key = even.get)
        max_odd = max(odd, key = odd.get)
        
        if max_even == max_odd:
            max_even_freq = even[max_even]
            max_odd_freq = odd[max_odd]
            
            even.pop(max_even)
            odd.pop(max_odd)
            next_max_even = max(even, key = even.get)
            next_mat_odd = max(odd, key = odd.get)

            if even[next_max_even] + max_odd_freq >= odd[next_mat_odd] + max_even_freq:
                max_even = next_max_even
                odd[max_odd] = max_odd_freq
            else:
                max_odd = next_mat_odd
                even[max_even] = max_even_freq
           
        return len(nums) - even[max_even] - odd[max_odd]