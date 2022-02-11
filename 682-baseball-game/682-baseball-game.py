class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        ops.reverse()
        
        while ops:
            temp = ops.pop()
            if temp == "+":
                record.append(record[-1] + record[-2])
            elif temp == "D":
                record.append(2*record[-1])
            elif temp == "C":
                record.pop()
            else:
                record.append(int(temp))
        
        return sum(record)