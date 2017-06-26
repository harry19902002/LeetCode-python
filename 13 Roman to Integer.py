class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        count = len(s)
        for i in xrange(count):
            thisStr = s[i]
            if i < count-1:
                nextStr = s[i+1]
            else:
                nextStr = 'Y'
            
            if thisStr == 'M':
                number += 1000
            elif thisStr == 'D':
                if nextStr == 'M':
                    number -= 500
                else:
                    number += 500
            elif thisStr == 'C':
                if (nextStr == 'D' or nextStr == 'M'):
                    number -= 100
                else:
                    number += 100
            elif thisStr == 'L':
                if nextStr == 'D' or nextStr == 'M' or nextStr == 'C':
                    number -= 50
                else:
                    number += 50
            elif thisStr == 'X':
                if nextStr == 'D' or nextStr == 'M' or nextStr == 'C'or nextStr == 'L':
                    number -= 10
                else:
                    number += 10
            elif thisStr == 'V':
                if nextStr == 'D' or nextStr == 'M' or nextStr == 'C'or nextStr == 'L'or nextStr == 'X':
                    number -= 5
                else:
                    number += 5
            elif thisStr == 'I':
                if nextStr != 'I' and nextStr != 'Y':
                    number -= 1
                else:
                    number += 1
        
        return number