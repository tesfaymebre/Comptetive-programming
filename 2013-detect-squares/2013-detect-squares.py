class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x_points = defaultdict(set)
        self.y_points = defaultdict(set)

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        
        self.points[point] += 1
        self.x_points[point[0]].add(point)
        self.y_points[point[1]].add(point)
        

    def count(self, point: List[int]) -> int:
        x, y = point
        p1 = (x,y)
        ans = 0 

        for p2 in self.x_points[x]:
            if p1 == p2:
                continue
            
            dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            
            for p3 in self.y_points[y]:
                if p3 == p1 or p3 == p2:
                    continue 
                
                dist1 = abs(p1[0] - p3[0]) + abs(p1[1] - p3[1])

                if dist != dist1:
                    continue 
                    
                p4 = (p3[0], p2[1])
                
                if self.points[p2] and self.points[p3] and self.points[p4]:
                    ans += self.points[p2]*self.points[p3]*self.points[p4]
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)