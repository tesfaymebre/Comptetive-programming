class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        prefix = [0]
        for i in range(len(customers)):
            if grumpy[i] == 0:
                prefix.append(prefix[-1] + customers[i])
            else:
                prefix.append(prefix[-1])
                
        normal_prefix = [0]
        for i in range(len(customers)):
            normal_prefix.append(normal_prefix[-1] + customers[i])
    
        max_customers = prefix[-1]
        for j in range(minutes,len(grumpy)+1):
            curr = prefix[-1] + normal_prefix[j] - normal_prefix[j-minutes] - (prefix[j] - prefix[j-minutes])
            max_customers = max(max_customers, curr)
            
        return max_customers