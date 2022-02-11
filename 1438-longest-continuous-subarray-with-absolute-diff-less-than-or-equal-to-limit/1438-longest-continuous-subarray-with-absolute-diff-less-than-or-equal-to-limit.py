class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        right = 0
        check_right = True  #in order to check whether the right pointer is updated or not 
        max_deq = deque()   
        min_deq = deque()
        length = 0
        
        while right < len(nums):
            #if max_deq and min_deq are empty
            if right == 0:
                max_deq.append(nums[right])
                min_deq.append(nums[right])
            #if right pointer is updated we can continue append on the max_deq and min_deq
            # otherwise we donot have to append nums[right] since we have already deal with             # this position
            elif check_right:
                #considering decreasing montonic queue
                while max_deq and max_deq[-1] < nums[right]:
                    max_deq.pop()
                    
                max_deq.append(nums[right])
                
                #considering increasing monotonic queue
                while min_deq and min_deq[-1] > nums[right]:
                    min_deq.pop()
                    
                min_deq.append(nums[right])
                
            #update length for the subarray wiht absolute diff less than/equal to limit    
            if abs(max_deq[0] - min_deq[0]) <= limit:
                length = max(length,right-left+1)
                right += 1
                check_right = True
            #if not just update left pointer and 
            # also check_right must be False since we didnot update right pointer 
            else:
                if max_deq[0] == nums[left]:
                    max_deq.popleft()
                    
                if min_deq[0] == nums[left]:
                    min_deq.popleft()
                    
                left += 1
                check_right = False
            
        return length
            
            
        