# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashTable = {}
        
        def helper(node):
            while (node != None):
                if (node in hashTable):
                    return True
                hashTable[node] = 1
                node = node.next

            hashTable[node] = 1
            return False
        
        return helper(head)