class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        window = defaultdict(list)
        freq = defaultdict(int)

        for idx, num in enumerate(nums):
            window[num].append(idx)
            freq[num] += 1

        min_size = len(nums)
        degree = max(freq.values())
        
        for num,count in freq.items():
            if count == degree:
                min_size = min(min_size, window[num][-1] - window[num][0] + 1)

        return min_size
        