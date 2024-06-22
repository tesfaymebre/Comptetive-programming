class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(n):
            if n == parent[n]:
                return n
            n = find(parent[n])
            return n


        def join(n1,n2):
            node1,node2 = find(n1),find(n2)
            if node1 == node2:
                return 
            if rank[node1] > rank[node2]:
                parent[node2] = node1
            elif rank[node2] > rank[node1]:
                parent[node1] = node2
            else:
                parent[node1] = node2
                rank[node2]+=1
            return 

        for a,b in edges:
            join(a,b)
        lengths = defaultdict(int)
        for i in range(n):
            lengths[find(i)]+=1

        component = list(lengths.values())
        prefix = []
        for number in component:
            prefix.append(prefix[-1]+number if prefix else number)
        ans = 0
        for i in range(len(component)-1,0,-1):
            ans+=(component[i]*prefix[i-1])
        return ans