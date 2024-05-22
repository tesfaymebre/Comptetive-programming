class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n, ways = len(s), []

        def visit(offset, way):
            if offset == n:
                ways.append(list(way))
            
            for i in range(offset, n):
                sub = s[offset:i + 1:]
                if sub == sub[::-1]:
                    way.append(sub)
                    visit(i + 1, way)
                    way.pop()
            
        visit(0, [])
        return ways