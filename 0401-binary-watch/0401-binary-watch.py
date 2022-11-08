class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        for hr in range(12):
            for minute in range(60):
                if (bin(hr)+bin(minute)).count('1') == turnedOn:
                    if minute < 10:
                        result.append(f'{hr}:0{minute}')
                    else:
                        result.append(f'{hr}:{minute}')
        return result