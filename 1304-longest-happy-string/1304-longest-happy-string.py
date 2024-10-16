class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0:
            heapq.heappush(heap,(-a,'a'))

        if b > 0:
            heapq.heappush(heap,(-b,'b'))

        if c > 0:
            heapq.heappush(heap,(-c,'c'))

        result = []

        while heap:
            count, c = heapq.heappop(heap)

            if len(result) >= 2 and result[-1] == c and result[-2] == c:
                if heap:
                    count2, c2 = heapq.heappop(heap)
                    result.append(c2)
                    count2 += 1

                    if count2 < 0:
                        heapq.heappush(heap,(count2, c2))
                else:
                    break
            else:
                result.append(c)
                count += 1

            if count < 0:
                heapq.heappush(heap,(count,c))

        return "".join(result)