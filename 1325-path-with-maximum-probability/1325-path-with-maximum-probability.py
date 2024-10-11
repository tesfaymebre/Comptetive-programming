class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i,(a,b) in enumerate(edges):
            graph[a].append((b,i))
            graph[b].append((a,i))
        
        probabilities = [0]*n
        probabilities[start_node] = 1
        processed = set()

        heap = [(-1,start_node)]

        while heap:
            p,node = heapq.heappop(heap)

            if node in processed:
                continue

            processed.add(node)

            for nei,idx in graph[node]:
                curr_p = succProb[idx] * (-p)
                if nei not in processed and curr_p > probabilities[nei]:
                    probabilities[nei] = curr_p
                    heapq.heappush(heap,(-curr_p,nei))

        return probabilities[end_node]
        