class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashTable = {}

        for char in magazine:
            if char in hashTable:
                hashTable[char] = hashTable[char] + 1
            else:
                hashTable[char] = 1
        
        for char in ransomNote:
            if char in hashTable:
                if hashTable[char] <= 0:
                    return False
                else:
                    hashTable[char] = hashTable[char] - 1
            else:
                return False
        
        return True