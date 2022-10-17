class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0]*(n)
        
        for fir,las,seats in bookings:
            prefix_sum[fir-1] += seats
            
            if las < n: prefix_sum[las] -= seats
                
        for i in range(1,n):
            prefix_sum[i] += prefix_sum[i-1]
            
        return prefix_sum