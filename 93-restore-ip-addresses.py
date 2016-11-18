# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
# 
# For example:
# Given "25525511135",
# 
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        Solution.ans = []
        sol = []
        self.dfs(s, 0, 4, sol)
        addresses = []
        for ip in Solution.ans:
            ip = '.'.join(ip)
            addresses.append(ip)
        return addresses
        
    def dfs(self, s, start, n, sol):
        if start == len(s) and n == 0:
            Solution.ans.append(sol[:])
        elif start > len(s) or n < 0:
            return
        elif start < len(s) and n > 0:
            for i in range(1,4):
                if int(s[start:start+i]) <= 255 and (s[start] != '0' or i == 1):
                    sol.append(s[start:start+i])
                    self.dfs(s, start+i, n-1, sol)
                    sol.pop()

if __name__ == "__main__":
    print Solution().restoreIpAddresses("25525511135")
    print Solution().restoreIpAddresses("0000")
    print Solution().restoreIpAddresses("010010")
