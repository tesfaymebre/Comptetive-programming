class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        targetFriendTime = times[targetFriend]
        times.sort()

        heap = []
        available = []
        
        for time in times:
            while heap and heap[0][0] <= time[0]:
                end,chair = heapq.heappop(heap)
                heapq.heappush(available,chair)

            chair = len(heap)
            if available:
                chair = heapq.heappop(available)
            
            heapq.heappush(heap,(time[1],chair))

            if time == targetFriendTime:
                return chair
        