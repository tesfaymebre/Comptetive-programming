class DSU:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1]*size
        
    def find(self,name_idx):
        if self.parent[name_idx] != name_idx:
            self.parent[name_idx] = self.find(self.parent[name_idx])
            
        return self.parent[name_idx]
        
    def union(self,a,b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if self.rank[root_a] < self.rank[root_b]:
            root_a,root_b = root_b,root_a
            
        self.parent[root_b] = root_a
        self.rank[root_a] += self.rank[root_b]
        
        return self.parent[root_a]
        
class Solution:
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        #union find solution
        
        size = len(accounts)
        union_find = DSU(size)
        
        email_to_name_idx = {}
        
        for name_idx in range(size):
            for email in accounts[name_idx][1:]:
                if email in email_to_name_idx:
                    union_find.union(email_to_name_idx[email],name_idx)
                
                email_to_name_idx[email] = union_find.parent[name_idx]
                
        result = defaultdict(list)
        
        for email,name_idx in email_to_name_idx.items():
            root_name_idx = union_find.find(name_idx)
            result[root_name_idx].append(email)
            
            
        ans = []
        
        for name_idx,emails in result.items():
            ans.append([accounts[name_idx][0]] + sorted(emails))
            
        return ans
    
    """
        # dfs solution
        
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
        """
                
       