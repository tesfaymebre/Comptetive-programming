class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        tree = defaultdict(int)
        count = 0
        
        for i in range(len(arr)):
            tree[arr[i]] += 1
            
            for k in range(i):
                if arr[i] % arr[k] == 0:
                    tree[arr[i]] = tree[arr[i]] + tree[arr[i]//arr[k]] *  tree[arr[k]]

            count = count + tree[arr[i]]
       
        return count % (10**9 + 7)