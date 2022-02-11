class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        letter_count = Counter(tasks)
        uniq_tasks = sorted(set(tasks), key = lambda x:letter_count[x])
        
        t = uniq_tasks.pop()
        idle = (letter_count[t] - 1) * n
        time = letter_count[t] + idle 
        
        while uniq_tasks:
            temp = uniq_tasks.pop()
             
            if letter_count[temp] == letter_count[t]:
                if idle != 0:
                    idle -= letter_count[temp] - 1
                    time += 1
                elif idle - letter_count[temp] <= 0:
                    time += letter_count[temp] - idle
                    idle = 0
            else:
                if idle - letter_count[temp] <= 0:
                    time += letter_count[temp] - idle
                    idle = 0  
                else:
                    idle -= letter_count[temp]
                
        return time
       
        
        
                
       