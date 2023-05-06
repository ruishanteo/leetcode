class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        test = ""
        maxLength = -1
        
        if (len(s) == 0):
            return 0
        elif(len(s) == 1):
            return 1

        for c in s:
            curr = "".join(c)

            if (curr in test):
                test = test[test.index(curr) + 1:]
            test = test + "".join(c)
            maxLength = max(len(test), maxLength)
        return maxLength