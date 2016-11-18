# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        from itertools import combinations
        l = range(n*2)
        combs = list(combinations(l[1:-1],n-1))
        invalid = []
        for comb in combs:
            t = 1
            for i in range(1,n*2-1):
                if i in list(comb):
                    t += 1
                else:
                    t -= 1
                if t < 0:
                    invalid.append(comb)
                    break
        print invalid
        for comb in invalid:
            combs.remove(comb)
        ans = []
        for comb in combs:
            #if comb[0] + n-2 <  
            string = [')'] *2*n
            string[0] = '('
            for pos in comb:
                string[pos] = '('
            ans.append(''.join(string))
        return ans

if __name__ == "__main__":
    print Solution().generateParenthesis(4)
