# Given a digit string, return all possible letter combinations that the number could represent.

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import itertools
        dic = [[' '],['*'],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        nums = []
        for char in digits:
            nums.append(dic[int(char)])
        letters = []
        for letter in itertools.product(*nums):
            letters.append(''.join(letter))
        return letters

if __name__ == "__main__":
    print Solution().letterCombinations('9')
