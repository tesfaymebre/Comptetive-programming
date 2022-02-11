class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        dic = {}
        order_num = 1
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(order_num)
                dic[order_num] = i
                order_num+=1
            elif s[i] == ')':
                start = dic[stack.pop()]
                end = i
                inner_s = " " + s[start +1 : end ] + " "
                s = s.replace(s[start : end +1], inner_s[::-1])
                
        return s.replace(" ","")