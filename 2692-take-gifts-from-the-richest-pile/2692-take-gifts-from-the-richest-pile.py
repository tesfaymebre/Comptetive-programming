class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        while k:
            heapq.heapreplace(heap,- floor(math.sqrt(-heap[0])))
            k -= 1

        return - sum(heap)


