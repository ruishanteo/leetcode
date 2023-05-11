# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
            
        stack = []
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        head = stack.pop()
        temp1 = head

        while stack:
            temp1.next = stack.pop()
            temp1 = temp1.next
 
        temp1.next = None

        return head