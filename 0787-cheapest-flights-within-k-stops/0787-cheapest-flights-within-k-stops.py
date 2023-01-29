class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        m = {}
        for f in flights:
            if f[0] not in m:
                m[f[0]] = []
            m[f[0]].append((f[1], f[2]))

        settled = {}

        h = [(0, src, 0)]
        
        while len(h) > 0:
            (cost, p, steps) = heappop(h)

            if p in settled and steps >= settled[p]:
                continue
           
            settled[p] = steps

            if p == dst:
               
                return cost

            if p in m:
                for f in m[p]:
                    cost1 = cost + f[1]
                    steps1 = steps + 1
                    p1 = f[0]
                    if steps1 <= k or p1 == dst:
                        
                        if p1 in settled and settled[p1] <= steps1:
                            continue
                        
                        heappush(h, (cost1, p1, steps1))

        return -1