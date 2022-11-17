class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        
        
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                graph[email].append(i)
                
                
        def dfs(i,emails):
            if i in visited:
                return
            
            visited.add(i)
            
            for email in accounts[i][1:]:
                emails.add(email)
                
                for neighbour in graph[email]:
                    dfs(neighbour,emails)
                    
            return
            
        visited = set()
        merged_accounts = []
        
        for i in range(len(accounts)):
            if i not in visited:
                emails = set()
                
                dfs(i,emails)
                merged_accounts.append([accounts[i][0]]+ sorted(emails))
                
        return merged_accounts