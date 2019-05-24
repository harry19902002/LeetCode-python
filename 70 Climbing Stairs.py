class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        s = 1
        m = 0
        for i in range(n):
            s,m = s+m,s
        return s