class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #x = abs(x)
        xList = list(str(x))
        xStr = ''.join(xList)

        xList.reverse()
        
        xReverseStr = ''.join(xList)
        
        print xStr
        print xReverseStr
        if xStr == xReverseStr:
            return True
        return False