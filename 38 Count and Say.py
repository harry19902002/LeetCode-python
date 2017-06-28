class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        nowStr = '1'
        nextStr = ''
        
        for i in range(1,n):
            print (nowStr)
            strNumber = nowStr[0]
            strCount = 0
            for content in nowStr:
                if content != strNumber:
                    nextStr += str(strCount)
                    nextStr += str(strNumber)
                    strCount = 1
                    strNumber = content
                else:
                    strCount += 1
            nextStr += str(strCount)
            nextStr += str(strNumber)
            nowStr = nextStr
            nextStr = ''
        
        return(nowStr)