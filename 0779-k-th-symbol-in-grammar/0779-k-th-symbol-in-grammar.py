class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def recursion(level, pos):
            if level==1:
                return 0
            
            prev_pos = (pos+1)//2
            get_prev = recursion(level-1, prev_pos)

            if pos&1:
                return get_prev
            else:
                return get_prev^1

        return recursion(n, k)