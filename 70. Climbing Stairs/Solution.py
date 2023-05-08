class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        hashTable = {}

        def helper(num):
            if num < 0:
                hashTable[num] = 0
                return 0
            elif num == 0:
                hashTable[num] = 1
                return 1
            else:
                if num in hashTable:
                    return hashTable[num]
                else:
                    hashTable[num] = helper(num - 1) + helper(num - 2) 
                    return hashTable[num]
        
        return helper(n)