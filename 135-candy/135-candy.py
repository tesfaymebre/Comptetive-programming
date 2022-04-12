class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)
        in_bound = lambda r: 0 <= r < len(ratings)
        
        for i in range(len(ratings)):
            if in_bound(i + 1) and ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
                res[i] = res[i+1] +1
            if in_bound(i-1) and ratings[i] > ratings[i-1] and res[i] <= res[i-1]:
                res[i] = res[i-1] + 1
        
        for j in range(len(ratings)-1,-1,-1):
            if in_bound(j + 1) and ratings[j] > ratings[j+1] and res[j] <= res[j+1]:
                res[j] = res[j+1] + 1
            if in_bound(j-1) and ratings[j] > ratings[j-1] and res[j] <= res[j-1]:
                res[j] = res[j-1] + 1
        return sum(res)