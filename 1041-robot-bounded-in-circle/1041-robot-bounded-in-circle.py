class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        distance = 0

        for instruction in instructions:
            if instruction == 'R':
                direction +=1
            elif instruction == 'L':
                direction +=3
            elif instruction == 'G':
                if direction < 2:
                    distance +=1
                elif direction > 1:
                    distance -=1

            direction %=4
                
        return direction != 0 or (distance == 0)