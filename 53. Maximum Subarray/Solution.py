class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        globalMaxSum = -math.pow(10, 4)
        localMaxSum = 0

        for i in range (len(nums)):
            localMaxSum = max(nums[i], nums[i] + localMaxSum)
            globalMaxSum = max(localMaxSum, globalMaxSum)
        return globalMaxSum