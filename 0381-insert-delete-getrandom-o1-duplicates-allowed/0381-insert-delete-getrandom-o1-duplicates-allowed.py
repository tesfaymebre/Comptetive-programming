class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.multiset = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.multiset[val].add(len(self.nums)-1)
        
        if len(self.multiset[val]) == 1:
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.multiset[val]:
            idx = self.multiset[val].pop()
            self.multiset[self.nums[-1]].add(idx)
            self.multiset[self.nums[-1]].remove(len(self.nums)-1)
            self.nums[idx] = self.nums[-1]
            self.nums.pop()
            return True
        return False
            
    def getRandom(self) -> int:
        random_index = random.randint(0,len(self.nums)-1)
        print(random_index)
        return self.nums[random_index]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()