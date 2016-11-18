# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

class Solution(object):
    def isMatch_recur(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) == 0:
            return len(s) == 0
        elif len(p) == 1:
            if len(s) != 1: return False
            if p[0] != '.' and p[0] != s[0]: return False
            else: return True
        else:
            if p[1] != '*':
                if len(s) < 1: return False
                if p[0] != '.' and p[0] != s[0]: return False
                else: return self.isMatch_recur(s[1:], p[1:])
            elif p[1] == '*':
                if self.isMatch_recur(s, p[2:]): return True
                i = 0
                while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                    if self.isMatch_recur(s[i+1:], p[2:]): return True
                    i += 1
                return False

    def isMatch(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for i in range(m + 1)]  # dp[i][j] is isMatch(s[:i-1], p[:j-1])
        dp[0][0] = True  
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j-1] != '.' and p[j-1] != '*':
                    if i > 0 and dp[i-1][j-1] and p[j-1] == s[i-1]:
                        dp[i][j] = True
                elif p[j-1] == '.':
                    if i > 0 and dp[i-1][j-1]:
                        dp[i][j] = True
                elif p[j-1] == '*' and j > 1:
                    if dp[i][j-2]:  # zero preceding element 
                        dp[i][j] = True
                    if dp[i][j-1]:  # one preceding element
                        dp[i][j] = True
                    if i > 0 and dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == '.'):
                        dp[i][j] = True
        return dp[m][n]

if __name__ == "__main__":
    import time
    start = time.clock()
    print Solution().isMatch_recur("aab", "c*a*b")
    end = time.clock()
    print ' '.join([str((end - start) * 1000), 'ms'])

    start = time.clock()
    print Solution().isMatch("aab", "c*a*b")
    end = time.clock()
    print ' '.join([str((end - start) * 1000), 'ms'])
