class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p1 =0
        p2 = len(people) - 1
        count = 0
        
        people.sort()
        
        while p1 <= p2:
            
            if people[p2] + people[p1] <= limit:
                p1 += 1  
                
            count += 1
            p2 -= 1
                
        return count