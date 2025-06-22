class UnionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]

        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return 0

        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_y] = parent_x
            self.rank[parent_x] += 1

        return 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        dsu = UnionFind(size)
        province = len(isConnected)

        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if row != col and isConnected[row][col]:
                    province -= dsu.union(row,col)

        return province