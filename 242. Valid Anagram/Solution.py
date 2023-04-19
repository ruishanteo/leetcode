class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sortedS = sorted(s)
        sortedT = sorted(t)
        if (len(s) != len(t)):
            return False
        else:
            return sortedS == sortedT