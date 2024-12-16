class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num,idx) for idx, num in enumerate(nums)]
        heapq.heapify(heap)

        while k:
            num,idx = heap[0]
            heapq.heapreplace(heap, (num*multiplier, idx))
            k -= 1

        for num,idx in heap:
            nums[idx] = num

        return nums
