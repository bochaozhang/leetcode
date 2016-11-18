# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26

# Given an encoded message containing digits, determine the total number of ways to decode it.

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                if s[i] == '0':
                    return 0
                else:
                    dp[i] = 1
            elif i == 1:
                if s[i] == '0':
                    if s[i-1] == '1' or s[i-1] == '2':
                        dp[i] = 1
                    else:
                        return 0
                else:
                    if s[i-1:i+1] <= '26':
                        dp[i] = 2
                    else:
                        dp[i] = 1
            else:
                if s[i] == '0':
                    if s[i-1] == '1' or s[i-1] == '2':
                        dp[i] = dp[i-2]
                    else:
                        return 0
                else:
                    if s[i-1:i+1] <= '26' and s[i-1:i+1] > '9':
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = dp[i-1]
        return dp[-1]

if __name__ == "__main__":
    print Solution().numDecodings("12345626")
    print Solution().numDecodings("12345627")
    print Solution().numDecodings("00")
    print Solution().numDecodings("01")
    print Solution().numDecodings("10")
    print Solution().numDecodings("110")
    print Solution().numDecodings("11010")
    print Solution().numDecodings("101")
