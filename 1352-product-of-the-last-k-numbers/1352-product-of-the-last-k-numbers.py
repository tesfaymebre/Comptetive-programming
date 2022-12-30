class ProductOfNumbers:

    def __init__(self):
        # self.q = []
        self.product = [[1, 0]]
    def add(self, num: int) -> None:
        # self.q.append(num)
        curr = self.product[-1][:]
        if num == 0:
            curr[1] += 1
        else:
            curr[0] *= num
        self.product.append(curr)

    def getProduct(self, k: int) -> int:
        last, curr = self.product[-1], self.product[-(k+1)]
        # print(last, curr)
        # return 0
        if last[1] - curr[1] == 0:
            return (last[0]//curr[0])
        else:
            return 0 
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)____