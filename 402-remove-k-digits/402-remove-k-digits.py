class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #if the length of num is same as k. we have to return 0
        if len(num) == k:
            return '0'
        
        #using increasing monotonic queue, 
        #remove digit when the increasing condition unfulfilled with considering the k value 
        queue = deque()
        
        for digit in num:
            #since the output mustn't contain leading zeroes. 
            #remove zero when it at the starting position 
            if queue and queue[0] == '0':
                queue.popleft()
                
            #arranging the increasing monotonic queue    
            while queue and k > 0:
                if digit < queue[-1]:
                    queue.pop()
                    k -= 1
                else:
                    break
                
            queue.append(digit)
        
        #if we still have k > 0; we can remove N last digits
        while queue and k > 0:
            queue.pop()
            k -= 1
            
        return ("".join(queue)) if queue else '0'
                