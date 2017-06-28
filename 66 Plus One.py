class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        outList = []
        length = len(digits)
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        carryOver = True
        outList.append(0)
        for i in xrange(1,length):
            if digits[length -i -1] == 9 and carryOver ==True:
                outList.append(0)
            elif carryOver == True: 
                outList.append(digits[length-i-1]+1)
                carryOver = False
            else:
                outList.append(digits[length-i-1])
        if carryOver == True:
            outList.append(1)
        outList.reverse()
        return outList