class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n = len(edges1) + 1
        m = len(edges2) + 1

        d1 = to_diameter(to_graph(edges1, n), n)
        d2 = to_diameter(to_graph(edges2, m), m)

        return max((d1 + 1) // 2 + (d2 + 1) // 2 + 1, d1, d2)

def to_graph(edges: List[List[int]], n: int) -> List[List[int]]:
    graph = [list() for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

def to_diameter(graph: List[List[int]], n: int) -> int:
    queue = deque()
    seen  = [False] * n
    start = 0
    diam  = 0

    for i in range(2):
        queue.append(start)
        seen[start] = True
        height = 0

        while queue:
            height += 1

            for _ in range(len(queue)):
                v = queue.popleft()
                start = v

                for u in graph[v]:
                    if not seen[u]:
                        seen[u] = True
                        queue.append(u)

        if i == 0:
            seen = [False] * n
        else:
            diam = height - 1

    return diam
        