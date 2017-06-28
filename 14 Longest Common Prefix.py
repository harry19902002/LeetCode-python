class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            output = ''
            return output
        
        prefix = list(strs[0])
        
        for context in strs:
            strList = list(context)
            for i,j in enumerate(prefix):
                ##如果前缀字母不一致，则删去后面内容
                if i < len(strList):
                    if j != strList[i]:
                        del prefix[i:]
                ##如果单词比较少，则删去后面内容
                else:
                    del prefix[i:]
                    
        output = ''.join(prefix)
        return output