# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        

        def helper(elem1, elem2):
            if (elem1 == None):
                return elem2
            
            if (elem2 == None):
                return elem1
            
            merged = None
            
            if (elem1.val <= elem2.val):
                merged = elem1
                merged.next = helper(elem1.next, elem2)
            else:
                merged = elem2
                merged.next = helper(elem1, elem2.next)
            
            return merged

        return helper(list1, list2)