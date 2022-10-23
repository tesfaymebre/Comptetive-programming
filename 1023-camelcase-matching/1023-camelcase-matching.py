class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for q in queries:
            val = True

            start = 0
            for i in range(0, len(q)):
                if start < len(pattern) and q[i] == pattern[start]:
                    start += 1
                    continue

                if q[i].isupper():
                    val = False
                    break

            if start < len(pattern):
                val = False

            res.append(val)

        return res
        