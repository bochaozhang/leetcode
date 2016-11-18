# Validate if a given string is numeric.

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        num = False
        dot = False
        exp = False
        for i in range(len(s)):
            if self.isDigit(s[i]):
                num = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or num == False:
                    return False
                exp = True
                num = False
            elif s[i] == '-' or s[i] == '+':
                if i > 0 and s[i-1] != 'e':
                    return False
            else:
                return False 
        return num

    def isDigit(self, c):
        if ord(c) >= 48 and ord(c) <= 57:
            return True
        else:
            return False

if __name__ == "__main__":
    print Solution().isNumber("0")
    print Solution().isNumber(" 0.1")
    print Solution().isNumber("2e")
    print Solution().isNumber("2e10e")
    print Solution().isNumber(".")
    print Solution().isNumber("0 0 1")
