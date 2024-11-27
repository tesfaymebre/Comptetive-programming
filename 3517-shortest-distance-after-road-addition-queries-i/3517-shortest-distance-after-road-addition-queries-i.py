class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(graph, start):
            queue = deque([start])
            visited = set()
            dist = 0

            while queue:
                size = len(queue)

                for j in range(size):
                    node = queue.popleft()

                    if node == n-1:
                        return dist + distances[start]

                    visited.add(node)
                    distances[node] = min(distances[node],distances[start] + dist)

                    for nei in graph[node]:
                        if nei not in visited:
                            queue.append(nei)

                dist += 1

            return dist

        graph = defaultdict(list)
        distances = [j for j in range(n)]

        for i in range(n-1):
            graph[i].append(i+1)

        ans = []
        mini = float('inf')

        for u,v in queries:
            graph[u].append(v)
            distances[v] = min(distances[u] + 1, distances[v])
            curr = bfs(graph, v)

            if ans:
                curr = min(ans[-1],curr)

            ans.append(curr)

        return ans