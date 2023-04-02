class Solution:
    def binarySearch(self,potions,spell,success):
        left = 0
        right = len(potions) - 1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if potions[mid]*spell >= success:
                right = mid - 1
            else:
                left = mid + 1
                
        return len(potions) - left
    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        pairs = []
        for spell in spells:
            pairs.append(self.binarySearch(potions,spell,success))
            
        return pairs
        