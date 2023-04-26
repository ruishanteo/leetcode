class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashTable = {}
        count = 0
        hold = 0
        for char in s:
            if char in hashTable:
                hashTable[char] = hashTable[char] + 1
            else:
                hashTable[char] = 1
        
        for key, item in hashTable.items():
            if item % 2 == 0:
                count += item
            elif item > 2:
                count += item - 1
                item = 1
                hold = 1
            else:
                hold = 1
        
        return count + hold