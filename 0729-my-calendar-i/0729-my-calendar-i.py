class MyCalendar:

    def __init__(self):
        self.my_calandar = []
        
    def binary_search_left(self,my_calandar,search):
        left,right = 0,(len(my_calandar)*2)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if my_calandar[mid//2][mid%2] < search:
                left = mid+1
            else:
                right = mid-1
                
        return left
        
    def book(self, start: int, end: int) -> bool:
        n = len(self.my_calandar)
        if not self.my_calandar:
            self.my_calandar.append([start,end])
            return True
        
        self.my_calandar.sort()
        start_position = self.binary_search_left(self.my_calandar,start)
        
        if start_position >= 2*n:
            self.my_calandar.append([start,end])
            return True
        if start_position%2 == 0 and end <= self.my_calandar[start_position//2][0]:
            self.my_calandar.append([start,end])
            return True
        elif start_position%2 == 1 and self.my_calandar[start_position//2][1] <= start:
            if start_position + 1 < 2*n:
                if self.my_calandar[(start_position+1)//2][0] >= end :
                    self.my_calandar.append([start,end])
                    return True
            else:
                self.my_calandar.append([start,end])
                return True
        return False
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)