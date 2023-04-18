class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        forward = ""
        backward = ""
        for i in s:
            if (i.isalnum()):
                forward = forward + i.lower()
                backward = i.lower() + backward 
        
        return forward == backward