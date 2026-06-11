class Solution {
    Map<Integer, List<Integer>> graph = new HashMap<>();
    Set<Integer> visited = new HashSet<>();

    public int assignEdgeWeights(int[][] edges) {
        for (int[] edge : edges){
            int u = edge[0];
            int v = edge[1];

            graph.computeIfAbsent(u,k -> new ArrayList<>()).add(v);
            graph.computeIfAbsent(v,k -> new ArrayList<>()).add(u);   
        }

        int max_depth = dfs(1);
        int MOD = 1_000_000_007;
        return (int) modPow(2, max_depth - 1, MOD);
    }

    public int dfs(int node){
        visited.add(node);
        
        int curr_depth = 0;

        for (int nei : graph.get(node)){
            if (!visited.contains(nei)){
                curr_depth = Math.max(curr_depth, 1 + dfs(nei));
            }
        }

        return curr_depth;
    }

    private long modPow(long base, long exp, long mod) {
        long result = 1;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }

        return result;
    }
}