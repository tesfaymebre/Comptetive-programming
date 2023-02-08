class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(set)

        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        ans = 0
        queue = deque([source])
        seenStop = set() 
        seenRoute = set() 
        seenStop.add(source) 

        while queue:
            for elem in range(len(queue)):
                stop = queue.popleft()
                
                if stop == target:
                    return ans
                
                for routeId in graph[stop]:
                    
                    if routeId not in seenRoute:
                        for newStop in routes[routeId]:
                            
                            if newStop not in seenStop:
                                queue.append(newStop)
                                seenStop.add(newStop)
                                
                        seenRoute.add(routeId)
            ans += 1
        return -1