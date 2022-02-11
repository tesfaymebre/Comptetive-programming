class Solution:
    def calculate(self, s: str) -> int:
        queue = deque()
        ps_ms = ('+','-')
        ts_dv = ('*','/')
        
        temp = ''
        multi = False
        div = False
        i = 0
        
        while i < len(s):
                
            if s[i].isdigit():
                temp += s[i]
                
                if i != len(s) - 1:
                    i += 1
                    continue
           
            if multi == True and temp != '':
                product = queue.pop() * int(temp)
                queue.append(product)
                temp = ''
                multi = False
                
            if div == True and temp != '':
                quotient = queue.pop() // int(temp)
                queue.append(quotient)
                temp = ''
                div = False
              
            if s[i] in ps_ms:
                
                if temp != '':
                    queue.append(int(temp))
                    
                temp = ''
                queue.append(s[i])
                
            if s[i] in ts_dv:
                
                if temp != '':
                    queue.append(int(temp))
                    
                temp = ''
                
                if s[i] == ts_dv[0]:
                    multi = True
                elif s[i] == ts_dv[1]:
                    div = True
                    
            i += 1
                    
        if i == len(s) and temp.isdigit():
            queue.append(int(temp))
        
        result = queue.popleft()
        
        while queue:
            t = queue.popleft()
            
            if t == '+':
                result += queue.popleft()
            elif t == '-':
                result -= queue.popleft()
                
        return result
       