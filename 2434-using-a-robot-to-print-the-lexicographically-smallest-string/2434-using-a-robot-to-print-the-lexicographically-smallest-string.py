class Solution:
    def robotWithString(self, s: str) -> str:
        my_dict = {}
        for i in range(len(s)):
            if s[i] not in my_dict:
                my_dict[s[i]] = []
            my_dict[s[i]].append(i)
        
        res = []
        pre = 0
        stack = []
        for i in range(26):
            cur_char = chr(ord('a') + i)
            if cur_char not in my_dict:
                continue
            
            for p_index in my_dict[cur_char]:
                if p_index < pre:
                    continue
                while len(stack) != 0 and ord(stack[len(stack)-1]) <= ord(cur_char):
                    res.append(stack.pop())
                res.append(cur_char)
                
                while pre < p_index:
                    stack.append(s[pre])
                    pre += 1
                pre = p_index+1
        
        while len(stack) != 0:
            res.append(stack.pop())
    
        return "".join(res)