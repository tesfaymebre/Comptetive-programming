class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.unfairness = float('inf')
        
        def backT(idx,distribution):
            if idx == len(cookies):
                self.unfairness = min(self.unfairness,max(distribution))
                return
            
            if self.unfairness <= max(distribution):
                return
            
            for i in range(k):
                distribution[i] += cookies[idx]
                backT(idx+1,distribution)
                distribution[i] -= cookies[idx]
                
            return
        
        cookies.sort(reverse = True)
        backT(0,[0]*k)
        return self.unfairness