class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed = deque(pushed)
        stack = []
        
        for i in range(len(popped)):
            if not stack:
                stack.append(pushed.popleft())
            
            while stack:
                    if stack[-1] == popped[i]:
                        stack.pop()
                        break 
                    if pushed:
                        stack.append(pushed.popleft())
                    else:
                        return False
        return True
                    
            