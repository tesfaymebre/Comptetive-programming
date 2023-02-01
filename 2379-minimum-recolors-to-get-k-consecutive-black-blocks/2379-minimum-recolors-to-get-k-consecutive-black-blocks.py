class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operation = len(blocks)
        white_count = 0
        left = 0
        
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                white_count += 1
                
            if right - left + 1 == k:
                min_operation = min(min_operation,white_count)
                
                if blocks[left] == 'W':
                    white_count -= 1
                    
                left += 1
                
        return min_operation
                
                