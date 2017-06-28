class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        ##Using dichotomy
        start = 0
        end = x
        mid = int(end / 2)
        state =False
        if x == 1:
            return 1
        while state==False:
            if mid * mid > x:
                end = mid
                state = False
                mid = int((start+end)/2)
            elif (mid+1) * (mid+1) < x+1:
                start = mid
                state = False
                mid = int((start+end)/2)
            else:state = True

        return mid