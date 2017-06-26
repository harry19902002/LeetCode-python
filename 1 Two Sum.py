class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        count = len(nums)
        for i in xrange(count):
            for j in xrange(i+1,count):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    return output
                    