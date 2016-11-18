# The count-and-say sequence is the sequence of integers beginning as follows:
# 1, 11, 21, 1211, 111221, ...

# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth sequence.

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            s = '1'
            for i in range(n-1):
                s = self.say(s)
        return s
        
    def say(self, s):
        if len(s) == 1:
            return ''.join(['1',s[0]])
        output = []
        count = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                output += [str(count)]
                output += [s[i-1]]
                count = 1
            else:
                count += 1
        output += [str(count), s[-1]]
        return ''.join(output)             

if __name__ == "__main__":
    print Solution().countAndSay(1)
    print Solution().countAndSay(2)
    print Solution().countAndSay(3)
    print Solution().countAndSay(4)
    print Solution().countAndSay(5)
    print Solution().countAndSay(6)
