# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        queue = deque([root])
        ans = []
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                if node:
                    ans.append(str(node.val))
                    
                    queue.append(node.left)
                    queue.append(node.right)
                    
                else:
                    ans.append("null")      
        
        return ' '.join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        data = data.split(" ")
        queue = deque()
        
        root = TreeNode(int(data[0]))
        queue.append(root)
        
        ptr = 1
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                node = queue.popleft()
                
                if ptr < len(data) and data[ptr] != 'null':
                    left = TreeNode(int(data[ptr]))
                    node.left = left
                    queue.append(left)
                    
                ptr += 1
                
                if ptr < len(data) and data[ptr] != 'null':
                    right = TreeNode(int(data[ptr]))
                    node.right = right
                    queue.append(right)
                    
                ptr += 1
                
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))