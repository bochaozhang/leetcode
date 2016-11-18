# Given two binary strings, return their sum (also a binary string).

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = []
        carry = 0
        i = -1
        while -i <= len(a) and -i <= len(b):
            s = int(a[i]) + int(b[i]) + carry
            if s >= 2:
                ans.append(s-2)
                carry = 1
            else:
                ans.append(s)
                carry = 0
            i -= 1
        while -i <= len(a):
            s = int(a[i]) + carry
            if s >= 2:
                ans.append(s-2)
                carry = 1
            else:
                ans.append(s)
                carry = 0
            i -= 1
        while -i <= len(b):
            s = int(b[i]) + carry
            if s >= 2:
                ans.append(s-2)
                carry = 1
            else:
                ans.append(s)
                carry = 0
            i -= 1
        if carry > 0:
            ans.append(carry)
        ans = map(str,ans)
        return ''.join(ans[::-1])
            
        
if __name__ == "__main__":
    print Solution().addBinary("11","1")
