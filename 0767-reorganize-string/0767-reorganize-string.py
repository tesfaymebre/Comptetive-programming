class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        freq = Counter(s)
        heap = [[-val, key] for key, val in freq.items()]
        
        heapq.heapify(heap)
        item = heapq.heappop(heap)

        while heap:
            ans.append(item[1])
            item[0] += 1 
            temp = heapq.heappop(heap)
            
            if item[0] < 0:
                heapq.heappush(heap,item)
           
            item = temp

        ans.append(item[1])
        
        return "".join(ans) if len(ans) == len(s) else ""