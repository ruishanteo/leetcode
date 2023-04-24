class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def helper(key, n):
            begin = 0
            end = n - 1
            while begin < end:
                mid = begin + (end - begin) / 2
                if (key <= nums[mid]):
                    end = mid
                else:
                    begin = mid + 1
            
            if (nums[begin] == key):
                return begin
            else:
                return -1
        
        return helper(target, len(nums))