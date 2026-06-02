class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def helper(start1, duration1, start2, duration2):
            total1 = float('inf')
            
            for i in range(len(start1)):
                total1 = min(total1, start1[i] + duration1[i])

            total2 = float('inf')

            for j in range(len(start2)):
                total2 = min(total2, max(total1, start2[j]) + duration2[j])

            return total2

        land_water = helper(landStartTime, landDuration, waterStartTime, waterDuration)
        water_land = helper(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_water, water_land)