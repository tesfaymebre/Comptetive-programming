class Solution:
    def findScore(self, nums: List[int]) -> int:
        sorted_nums = [(x,i) for i,x in enumerate(nums)]
        sorted_nums.sort()
        marked = set()
        score = 0

        for x,i in sorted_nums:
            if i not in marked:
                score += x
                marked.add(i)
                marked.add(i-1)
                marked.add(i+1)

        return score