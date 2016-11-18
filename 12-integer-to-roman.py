# Given an integer, convert it to a roman numeral.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        quo = num / 1000
        roman += 'M' * quo
        num -= quo * 1000
        
        quo = num / 100
        if quo == 9: roman += 'C' + 'M'
        elif quo >= 5 and quo < 9: roman += 'D' + 'C' * (quo-5)
        elif quo == 4: roman += 'C' + 'D'
        else: roman += 'C' * quo
        num -= quo * 100
         
        quo = num / 10
        if quo == 9: roman += 'X' + 'C'
        elif quo >= 5 and quo < 9: roman += 'L' + 'X' * (quo-5)
        elif quo == 4: roman += 'X' + 'L'
        else: roman += 'X' * quo
        num -= quo * 10

        if num == 9: roman += 'I' + 'X'
        elif num >= 5 and num < 9: roman += 'V' + 'I' * (num-5)
        elif num == 4: roman += 'I' + 'V'
        else: roman += 'I' * num    
        
        return roman

if __name__ == '__main__':
    print Solution().intToRoman(8)
    print Solution().intToRoman(1954)
    print Solution().intToRoman(1990)
    print Solution().intToRoman(2014)
    print Solution().intToRoman(123)
    
