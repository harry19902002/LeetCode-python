class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        count = len(s)
        for i in xrange(count):
            if s[i] == 'M':
                number += 1000
            elif s[i] == 'D':
                if s[i+1] == 'M':
                    number -= 500
                else:
                    number += 500
            elif s[i] == 'C':
                if (s[i+1] == 'D' || s[i+1] == 'M'):
                    number -= 100
                else:
                    number += 100
            elif s[i] == 'L':
                if s[i+1] == 'D' || s[i+1] == 'M' || s[i+1] == 'C':
                    number -= 50
                else:
                    number += 50
            elif s[i] == 'X':
                if s[i+1] == 'D' || s[i+1] == 'M' || s[i+1] == 'C'|| s[i+1] == 'L':
                    number -= 10
                else:
                    number += 10
            elif s[i] == 'V':
                if s[i+1] == 'D' || s[i+1] == 'M' || s[i+1] == 'C'|| s[i+1] == 'L'|| s[i+1] == 'X':
                    number -= 5
                else:
                    number += 5
            elif s[i] == 'I':
                if s[i+1] != 'I':
                    number -= 1
                else:
                    number += 1
        
        return number