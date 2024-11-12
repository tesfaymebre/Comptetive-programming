class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        maxi_beauty = [0]

        for price, beauty in items:
            maxi_beauty.append(max(maxi_beauty[-1],beauty))

        n = len(items)
        ans = []

        def r_binary_search(val):
            left = 0
            right = n - 1

            while left <= right:
                mid = left + (right - left) // 2

                if items[mid][0] <= val:
                    left = mid + 1
                else:
                    right = mid - 1

            return left

        for j in queries:
            idx = r_binary_search(j)
            ans.append(maxi_beauty[idx])

        return ans