# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
# 
# You have the following 3 operations permitted on a word:
# 
# a) Insert a character
# b) Delete a character
# c) Replace a character

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for x in range(m+1)] for y in range(n+1)]
        for i in range(m+1):
           dp[0][i] = i
        for j in range(n+1):
            dp[j][0] = j
        for i in range(1,m+1):
            for j in range(1,n+1):
                k = 0
                if word1[i-1] != word2[j-1]: k = 1
                dp[j][i] = min(dp[j-1][i]+1, dp[j][i-1]+1, dp[j-1][i-1]+k)
        return dp[n][m]

if __name__ == "__main__":
    print Solution().minDistance("cat","dots") 
    print Solution().minDistance("","") 
    print Solution().minDistance("a","") 
