class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        occurance = Counter(arr1)
        temp = []
        for x in arr2:
            for j in range(occurance[x]):
                temp.append(x)
                arr1.remove(x)
        arr1.sort()
        temp.extend(arr1)
        return temp
