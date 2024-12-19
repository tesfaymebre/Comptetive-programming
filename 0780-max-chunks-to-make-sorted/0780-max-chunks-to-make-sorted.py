class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        temp = set()
        chunks = 0

        for i in range(len(arr)):
            temp.add(arr[i])
            n = len(temp)
            
            for j in range(i-n+1,i+1):
                if j not in temp:
                    break
            else:
                chunks += 1
                temp = set()

        if temp:
            chunks += 1

        return chunks