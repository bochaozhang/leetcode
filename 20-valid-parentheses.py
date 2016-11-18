# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list = []
        for char in s:
            if char == '(': list.append('P')
            if char == '[': list.append('B')
            if char == '{': list.append('C')
            if char == ')':
                if len(list) == 0: return False
                if list[-1] != 'P': return False
                del list[-1]
            if char == ']':
                if len(list) == 0: return False
                if list[-1] != 'B': return False
                del list[-1]
            if char == '}':
                if len(list) == 0: return False
                if list[-1] != 'C': return False
                del list[-1]
        if len(list) != 0:
            return False
        return True    

if __name__ == "__main__":
    print Solution().isValid('({[]})')
    print Solution().isValid('({[]}))')
    print Solution().isValid('({[}])')
