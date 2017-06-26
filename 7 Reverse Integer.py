class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = x* (-1)
        xList = list(str(x))
        xList.reverse()
        print (xList)
        output = ''.join(xList)
        if int(output) > 2147483647:
            return 0
        if isNegative == True:
        	return -int(output)
        return int(output)