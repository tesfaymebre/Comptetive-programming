class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for x in tokens:
            if x.isdigit() or (x[0] == "-" and x[1:].isdigit()):
                stack.append(int(x))
            else:
                op2, op1 = stack.pop(), stack.pop() #set second_operad and first_operad
                if x == "+":
                    stack.append(op1 + op2)
                elif x == "-":
                    stack.append(op1 - op2)
                elif x == "*":
                    stack.append(op1 * op2)
                elif x == "/":
                    stack.append(int(op1/op2))
                
        return stack.pop()