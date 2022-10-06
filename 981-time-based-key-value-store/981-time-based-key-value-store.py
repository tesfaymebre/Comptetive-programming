class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        n = len(self.d[key])
        left,right = 0,n-1
        temp = ""
        
        while left <= right:
            mid = left + (right - left)//2
            
            if self.d[key][mid][0] == timestamp:
                return self.d[key][mid][1]
            elif self.d[key][mid][0] < timestamp:
                temp = self.d[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
                  
        return temp


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)