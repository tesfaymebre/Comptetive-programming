class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        rec = [0]*len(temperatures)
        dic = {}
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                indx= stack.pop()
                rec[indx]= i - indx
            stack.append(i)
        
        return rec