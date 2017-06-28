class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = len(nums)
        index = 0
        for i in xrange(1,count):
            if nums[i - index] == nums[i - 1 - index]:
                print(i)
                del nums[i - index]
                count -= 1
                index += 1
                
        return count