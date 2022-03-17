class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        
        freq = defaultdict(int)
        self.curr_lead = dict()
        leader = persons[0]
        
        for i in range(len(persons)):
            freq[persons[i]] += 1
            
            if freq[leader] <= freq[persons[i]]:
                leader = persons[i]
                
            self.curr_lead[i] = leader

    def q(self, t: int) -> int:
        indx = 0
        left = 0
        right = len(self.times) - 1
        
        while left <= right:
            mid = left + (right - left)//2
            
            if self.times[mid] <= t:
                left = mid + 1
                indx = mid
            else:
                right = mid - 1
                
        return self.curr_lead[indx]

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)