# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i in range(len(s)):
            if s[i] == 'I':
                if i < len(s) - 1 and (s[i+1] == 'V' or s[i+1] == 'X'):
                    r -= 1
                else:
                    r +=1
            if s[i] == 'X':
                if i < len(s) - 1 and (s[i+1] == 'L' or s[i+1] == 'C'):
                    r -= 10
                else:
                   r +=10
            if s[i] == 'C':
                if i < len(s) - 1 and (s[i+1] == 'D' or s[i+1] == 'M'):
                    r -= 100
                else:
                    r +=100
            if s[i] == 'V':
                r += 5
            if s[i] == 'L':
                r += 50
            if s[i] == 'D':
                r += 500
            if s[i] == 'M':
                r += 1000
        return r

if __name__ == "__main__":
    print Solution().romanToInt("MCMLIV")
    print Solution().romanToInt("MCMXC")
    print Solution().romanToInt("XI")
    print Solution().romanToInt("MMXIV")
    print Solution().romanToInt("IIIV")
