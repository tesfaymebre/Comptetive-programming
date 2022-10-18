class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix_sum = [0]*(1001)
        
        for passengers,start,to in trips:
            prefix_sum[start] += passengers
            prefix_sum[to] -= passengers
            
        if prefix_sum[0] > capacity:
            return False
        
        for i in range(1,1001):
            prefix_sum[i] += prefix_sum[i-1]
            if prefix_sum[i] > capacity:
                return False
            
        return True