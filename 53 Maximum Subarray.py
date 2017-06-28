class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        thisSum = nums[0]
        length = len(nums)
        
        if thisSum < 0:
            thisSum = 0
        
        for i in nums[1:]:
            thisSum += i
            
            if thisSum >= maxSum:
                maxSum = thisSum 
                
            if thisSum < 0:
                thisSum = 0
            
        return maxSum