# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_diameter = 0
        self.findMaxDepth(root)
        return self.max_diameter
    
    def findMaxDepth(self, root):
        if not root:
            return 0
        left_depth = self.findMaxDepth(root.left)
        right_depth = self.findMaxDepth(root.right)
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)