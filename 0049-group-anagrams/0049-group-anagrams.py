class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ancestor = defaultdict(list)
        
        for word in strs:
            ancestor["".join(sorted(word))].append(word)
        
        return [group for key,group in ancestor.items()]