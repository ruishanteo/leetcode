# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(node):
            if (node == None):
                return node

            if (node.val > p.val and node.val > q.val):
                return helper(node.left)
            
            if (node.val < p.val and node.val < q.val):
                return helper(node.right)
                
            return node
        
        return helper(root)