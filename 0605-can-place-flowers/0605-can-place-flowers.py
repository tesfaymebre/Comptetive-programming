class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                p1, p2 = i - 1, i + 1
                
                if p1 < 0 and p2 >= len(flowerbed):
                    n -= 1
                elif p1 < 0 and flowerbed[p2] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif p2 >= len(flowerbed) and flowerbed[p1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif flowerbed[p1] == 0 and flowerbed[p2] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return True if n <= 0 else False
                    