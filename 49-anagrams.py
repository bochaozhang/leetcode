# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            if word not in dic:
                dic[word] = [i]
            else:
                dic[word].append(i)
        ans = []
        for item in dic:
            ans.append(sorted([strs[x] for x in dic[item]]))
        return ans

if __name__ == "__main__":
    print Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
