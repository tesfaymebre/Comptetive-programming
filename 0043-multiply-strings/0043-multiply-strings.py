class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        
        arr = []
        
        for i in range(len(num1)-1,-1,-1):
            curr = "0"*(len(num1)-i-1)
            carry = 0
            
            for j in range(len(num2)-1,-1,-1):
                temp = int(num1[i])*int(num2[j]) + carry
                
                curr += str(temp%10)
                carry = temp//10
            
            if carry > 0:
                curr += str(carry)
                
            arr.append(curr+"0"*(i+1))
             
        result = ''
        carry = 0
        
        for i in range(len(arr[-1])-1):
            curr = 0
            
            for j in range(len(arr)):
                curr += int(arr[j][i])
            
            curr += carry
            result += str(curr%10)
            carry = curr//10
            
        if carry > 0:
            result += str(carry)[::-1]
        
        return result[::-1]