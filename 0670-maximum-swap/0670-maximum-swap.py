class Solution:
    def maximumSwap(self, num: int) -> int:
        array = list(str(num))
        
        for i in range(len(array)):
            max_idx = i

            for j in range(i + 1, len(array)):

                if array[j] >= array[max_idx]:
                    max_idx = j
            
            if array[i] != array[max_idx]:
                array[i], array[max_idx] = array[max_idx], array[i]
                break
                
        return int("".join(array))
