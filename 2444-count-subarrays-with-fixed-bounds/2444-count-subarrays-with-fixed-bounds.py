class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minFound = False
        maxFound = False
        start = 0
        minStart = 0
        maxStart = 0
        count = 0

        for i,num in enumerate(nums):
            if num>maxK or num<minK:
                minFound = False
                maxFound = False
                start = i + 1
                
            if num == minK:
                minStart = i
                minFound = True
                
            if num == maxK:
                maxStart = i
                maxFound = True
                
            if minFound and maxFound:
                count+=min(minStart,maxStart)-start+1

        return count