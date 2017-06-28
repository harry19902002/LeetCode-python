class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        bias = 0
        for i in range(length):
            if nums[i - bias] == val:
                del nums[i -bias]
                bias += 1
        return len(nums)