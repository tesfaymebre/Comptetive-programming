class RecentCounter:

    def __init__(self):
        #setting up deque to have "first in first out" principle of "queue"
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        low_interval = t-3000   
        
        while self.requests[0] < low_interval:
            self.requests.popleft()
                
        return len(self.requests)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)