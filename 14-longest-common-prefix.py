# Write a function to find the longest common prefix string amongst an array of strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [] or strs == [""]:
            return ""
        l = map(len,strs)
        prefix = []
        for i in range(min(l)):
            keys = {}
            for j in range(len(strs)):
                keys[strs[j][i]] = 1
            if len(keys.keys()) == 1:
                prefix.append(keys.keys()[0])
            else:
                return "".join(prefix)
        return "".join(prefix)

if __name__ == "__main__":
    print Solution().longestCommonPrefix([])
    print Solution().longestCommonPrefix([""])
    print Solution().longestCommonPrefix(["a"])
    print Solution().longestCommonPrefix(['at','apple','ass'])
    print Solution().longestCommonPrefix(['abcst','abcpple','abcsass'])
    print Solution().longestCommonPrefix(['at','apple','bss'])
