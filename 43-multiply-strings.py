# Given two numbers represented as strings, return multiplication of the numbers as a string.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '' or num2 == '':
            return ''
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = num1[::-1]
        num2 = num2[::-1]
        product = ['0'] * (len(num1) + len(num2))
        for i in range(len(num1)):
            carry = 0
            for j in range(len(num2)):
                carry += int(num1[i]) * int(num2[j]) + int(product[i+j])
                product[i+j] = str(carry % 10)
                carry /= 10
            if carry != 0:
                product[len(num2)+i] = str(carry)
        product = product[::-1]
        for i in range(len(product)):
            if product[i] == '0':
                del product[i]
            if product[i] != '0':
                break
        return ''.join(product)

if __name__ == "__main__":
    print Solution().multiply("321", "43")
    print Solution().multiply("0", "0")
