class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return strs
        
        prefix = list(strs[0])
        print prefix
        
        for context in strs:
            strList = list(context)
            for i,j in prefix:
                if j != strList[i]:
                    del prefix[i]
                    
        output = ''.join(prefix)
        return output