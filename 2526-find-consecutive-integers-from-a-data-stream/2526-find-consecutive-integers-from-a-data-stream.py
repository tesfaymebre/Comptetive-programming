class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.target = value
        self.n_cons = 0

    def consec(self, num: int) -> bool:
        if num == self.target:
            self.n_cons += 1
        else:
            self.n_cons = 0
        
        return self.n_cons >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)