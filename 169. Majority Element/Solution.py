class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        count = 1
        for i in range (len(nums)):
            if nums[index] == nums[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                index = i
                count = 1
        
        return nums[index]