class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        indexes = [i for i in range(len(groupSizes))]
        indexes.sort(key = lambda x: groupSizes[x])
        result = []
        left = 0
        
        while left < len(groupSizes):
            result.append(indexes[left:left+(groupSizes[indexes[left]])])
            left = left + groupSizes[indexes[left]]
            
        return result