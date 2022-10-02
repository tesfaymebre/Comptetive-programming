class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # ans to return
        ans = []

        # Get the frequency of number in the list barcodes
        freq = collections.Counter(barcodes)

        # Create a max-heap based on frequency and notice the "- val" in order to make max heap. by         #default heapify works for min heap. so in order to have max heap we should negate the               #value.
        heap = [[-val, key] for key, val in freq.items()]

        # Heapify the heap
        heapq.heapify(heap)

        # Get the first item
        item = heapq.heappop(heap)

        while heap:
            ans.append(item[1])
            
            # "Decrease" the frequency (remember our frequency is negative, that's why we add)
            item[0] += 1 
            
            #hold the next varcode which is not equal with its previous barcode
            temp = heapq.heappop(heap)
            
            #push item back to heap if item[1]s count is not equal to zero
            if item[0] < 0:
                heapq.heappush(heap,item)
           
            item = temp

        # One item will remain outside of the while loop, we should append the last element!
        ans.append(item[1])

        return ans