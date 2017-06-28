class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count = len(s)
        
        bracketsContainer = []
        
        for content in s:
            if content == '{':
                bracketsContainer.append('Brace')
            if content == '[':
                bracketsContainer.append('SquareBracket')
            if content == '(':
                bracketsContainer.append('Bracket')
                
            if content == ')':
                if bracketsContainer == []:
                    return False
                if bracketsContainer[-1] != 'Bracket':
                    return False
                else:
                    del bracketsContainer[-1]
            if content == ']':
                if bracketsContainer == []:
                    return False                
                if bracketsContainer[-1] != 'SquareBracket':
                    return False
                else:
                    del bracketsContainer[-1]
            if content == '}':
                if bracketsContainer == []:
                    return False                
                if bracketsContainer[-1] != 'Brace':
                    return False
                else:
                    del bracketsContainer[-1]
        
        if bracketsContainer == []:
            return True
        else:
            return False