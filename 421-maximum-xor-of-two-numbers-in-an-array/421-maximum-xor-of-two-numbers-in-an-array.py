class TrieNode():
    def __init__(self):
        self.children = dict()
        self.curr_num = 0
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,num):
        curr = self.root
        
        for b in range(31,-1,-1):
            bit = '1' if (num & (1<<b)) >= 1 else '0' 
            
            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            
            curr = curr.children[bit]
            
        curr.curr_num = num
    
    def search(self,num):
        curr = self.root
        
        for b in range(31,-1,-1):
            bit = '1' if (num & (1<<b)) >= 1 else '0'
            bit_comp = '0' if bit == '1' else '1'
            
            if bit_comp in curr.children:
                curr = curr.children[bit_comp]
            else:
                curr = curr.children[bit]
           
        return curr.curr_num ^ num
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(num)
            
        max_XOR = 0
        
        for num in nums:
            max_XOR = max(max_XOR,self.search(num))
        
        return max_XOR
        