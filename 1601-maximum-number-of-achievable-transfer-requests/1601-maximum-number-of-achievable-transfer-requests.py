class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def backT(idx,net_change,num_requests):
            if idx == len(requests):
                for change in net_change:
                    if change != 0:
                        return 0
                        
                return num_requests
            
            from_building,to_building = requests[idx]
            net_change[from_building] -= 1
            net_change[to_building] += 1
            
            num_requests_included = backT(idx+1,net_change,num_requests+1)
            
            net_change[from_building] += 1
            net_change[to_building] -= 1
            
            num_requests_not_included = backT(idx+1,net_change,num_requests)
            
            return max(num_requests_included,num_requests_not_included)
        
        return backT(0,[0]*n,0)