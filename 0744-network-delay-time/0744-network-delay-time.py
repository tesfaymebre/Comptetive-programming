class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {node: float('inf') for node in range(1,n+1)}
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        distances[k] = 0
        heap = [(0,k)]
        processed = set()

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)

            if curr_node in processed:
                continue

            processed.add(curr_node)

            for nei,w in graph[curr_node]:
                new_dist = curr_dist + w

                if new_dist < distances[nei]:
                    distances[nei] = new_dist
                    heapq.heappush(heap,(new_dist,nei))

        if len(processed) < n:
            return -1

        min_time = 0

        for val in distances.values():
            min_time = max(min_time, val)

        return min_time

        