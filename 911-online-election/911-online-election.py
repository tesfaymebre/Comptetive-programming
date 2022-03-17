class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        
        freq = defaultdict(int)
        self.curr_lead = dict()
        leader = self.persons[0]
        for i in range(len(self.persons)):
            freq[self.persons[i]] += 1
            if freq[leader] <= freq[self.persons[i]]:
                leader = self.persons[i]
            self.curr_lead[i] = leader

    def q(self, t: int) -> int:
        indx = 0
        left = 0
        right = len(self.persons) - 1
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