class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Our ans to return
        ans = []

        # Get the freq
        freq = collections.Counter(barcodes)

        # Create a max-heap based on frequency
        heap = [[-val, key] for key, val in freq.items()]

        # Heapify the heap
        heapq.heapify(heap)

        # Get the first item
        item = heapq.heappop(heap)

        while heap:
            ans.append(item[1])
            item[0] += 1 # "Decrease" the count (remember our count is negative for min-heap, that's why we add)

            """
            'heapreplace' will pop the next item onto the heap, then push the old item!
            Its the secret weapon for this solution.
            We heappop if we don't want to push 'item' back onto the heap.
            """
            temp = heapq.heappop(heap)
            
            if item[0] < 0:
                heapq.heappush(heap,item)
            # item = heapq.heapreplace(heap, [item[0], item[1]]) if item[0] < 0 else heapq.heappop(heap)
            item = temp

        # Because I do a `heappop` outside of the while loop, we should append the last element!
        ans.append(item[1])

        return ans