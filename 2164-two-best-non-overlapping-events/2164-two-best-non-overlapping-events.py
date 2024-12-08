class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        def bisect_left(target):
            left = 0
            right = len(events) - 1
            best = len(events)

            while left <= right:
                mid = left + (right - left)//2

                if events[mid][0] >= target:
                    right = mid - 1
                    best = mid
                else:
                    left = mid + 1

            return best

        events.sort()
        max_vals = [events[-1][2]]

        for j in range(len(events)-2,-1,-1):
            max_vals.append(max(max_vals[-1],events[j][2]))

        max_vals = max_vals[::-1]

        max_sum = events[0][2]

        for i in range(len(events)):
            non_overlap_idx = bisect_left(events[i][1] + 1)
            val = max_vals[non_overlap_idx] if non_overlap_idx < len(events) else 0
            max_sum = max(max_sum, events[i][2] + val)

        return max_sum