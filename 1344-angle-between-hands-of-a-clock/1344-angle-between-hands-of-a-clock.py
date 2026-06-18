class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0

        hour_position = (hour * 5) + (minutes / 60) * 5

        return  min(abs(minutes - hour_position), 60 - minutes + hour_position, 60 - hour_position + minutes) * 6
