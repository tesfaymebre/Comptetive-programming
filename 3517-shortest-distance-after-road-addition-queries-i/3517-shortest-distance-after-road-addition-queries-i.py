class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(graph):
            queue = deque([0])
            visited = set()
            dist = 0

            while queue:
                size = len(queue)
                
                for j in range(size):
                    node = queue.popleft()
                    visited.add(node)

                    if node == n-1:
                        return dist

                    for nei in graph[node]:
                        if nei not in visited:
                            queue.append(nei)

                dist += 1

            return dist

        graph = defaultdict(list)

        for i in range(n-1):
            graph[i].append(i+1)

        ans = []

        for u,v in queries:
            graph[u].append(v)
            ans.append(bfs(graph))

        return ans