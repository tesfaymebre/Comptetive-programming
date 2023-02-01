class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def checker(subarray):
            diff = subarray[1] - subarray[0]
            
            for i in range(1,len(subarray)):
                if subarray[i] - subarray[i-1] != diff:
                    return False
                
            return True
        
        answer=[]
        for i in range(len(l)):
            subarray = nums[l[i]:r[i]+1]
            subarray.sort()
            answer.append(checker(subarray))
            
        return answer
        