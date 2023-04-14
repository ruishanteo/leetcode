class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashTable:
                return [hashTable[diff], i]
            else:
                hashTable[nums[i]] = i