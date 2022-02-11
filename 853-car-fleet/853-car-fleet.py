class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # find the time required to arrive to the target position.
        # since time = distance / speed
        time = [(pos,((target - pos)/v)) for pos,v in zip(position,speed)]
        
        #sort the time in reverse order based on position
        time.sort(key = lambda x: -x[0])
        stack = []
        
        for pos,t in time:
            if not stack:
                stack.append(t)
            elif t > stack[-1]:    # if t > stack[-1] their is no way the car become fleet   
                stack.append(t)
        
        return len(stack)
                