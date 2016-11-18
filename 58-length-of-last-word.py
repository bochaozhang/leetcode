# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip(' ')
        n = 0
        for i in reversed(range(len(s))):
            if s[i] == ' ':
                break
            n += 1
        return n

if __name__ == "__main__":
    print Solution().lengthOfLastWord("")
    print Solution().lengthOfLastWord(" ")
    print Solution().lengthOfLastWord("a ")
    print Solution().lengthOfLastWord("Hello World")
