class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        freq = Counter(candidates)
        res = []
        uniq = list(set(x for x in candidates))
        
        def backT(indx,total,path):
            if total == target:
                res.append(path)
                return
            
            if total > target:
                return
            
            for i in range(indx,len(uniq)):
                if freq[uniq[i]] == 0:
                    continue
                
                freq[uniq[i]] -= 1
                backT(i,total + uniq[i], path + [uniq[i]])
                freq[uniq[i]] += 1
                
            
        backT(0,0,[])
        return res