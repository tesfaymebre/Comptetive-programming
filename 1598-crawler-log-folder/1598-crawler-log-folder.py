class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for op in logs:
            if op != "../" and op != "./":
                stack.append(op)
            elif stack and op == "../":
                stack.pop()
        
        return len(stack)