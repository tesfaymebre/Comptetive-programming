class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in range(len(image)):
            end = len(image[0])-1
            for c in range(len(image[0])//2):
                image[r][c],image[r][end] = image[r][end],image[r][c]
                end -= 1
                
        for r in range(len(image)):
            for c in range(len(image[0])):    
                image[r][c] = 1 if image[r][c] == 0 else 0
                
                
        return image