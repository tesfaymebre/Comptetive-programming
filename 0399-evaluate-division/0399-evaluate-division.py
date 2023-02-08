class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacents = defaultdict(list)
        val_map = {}
        
        for i, (p, c) in enumerate(equations):
            adjacents[p].append(c)
            adjacents[c].append(p)
            val_map[(p, c)] = values[i]
            val_map[(c, p)] = 1 / values[i] 
        
        res = []
        def dfs(node, target, acc, visited):
            if node == target:
                res.append(acc)
                return True
            
            if node in visited:
                return False
            visited.add(node)
            
            for neighbor in adjacents[node]:
                if dfs(neighbor, target, acc * val_map[(node, neighbor)], visited):
                    return True
            
            return False
        
        for tp, tc in queries:
            if tp not in adjacents or tc not in adjacents:
                res.append(-1)
            else:
                solution_found = dfs(tp, tc, 1, set())
                if not solution_found:
                    res.append(-1)
        
        return res