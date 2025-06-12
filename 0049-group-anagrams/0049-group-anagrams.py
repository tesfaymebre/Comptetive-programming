class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            freq = [0]*26

            for c in s:
                freq[ord(c) - ord('a')] += 1

            groups[tuple(freq)].append(s)

        return [val for val in groups.values()]