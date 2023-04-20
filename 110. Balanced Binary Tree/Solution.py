# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node):
            if (node == None):
                return -1
            left_height = height(node.left)
            right_height = height(node.right)
            return max(left_height, right_height) + 1
        
        def helper(node):
            if (node == None):
                return True
            elif (abs(height(node.left) - height(node.right)) < 2):
                return helper(node.left) and helper(node.right)
            else:
                return False
        
        return helper(root)