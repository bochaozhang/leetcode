class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        numColumns = len(s) / (numRows * 2 -2) * 2
        if len(s) % (numRows * 2 - 2) > 0:
            numColumns += 1
        if len(s) % (numRows * 2 - 2) > numRows:
            numColumns += 1
        m = []
        n = 0
        for i in range(numColumns):
            column = []
            if i % 2 == 0:
                for j in range(numRows):
                    if n < len(s):
                        column.append(s[n])
                    else:
                        column.append(' ')
                    n += 1
            else:
                column.append(' ')
                for j in range(1,numRows-1):
                    if n < len(s):
                        column.append(s[n])
                    else:
                        column.append(' ')
                    n += 1
                column.append(' ')       
                column.reverse()
            m.append(column)
        r = []
        for i in range(numRows):
            for j in range(numColumns):
                if m[j][i] != ' ':
                    r.append(m[j][i])    
        return ''.join(r)

if __name__ == "__main__":
    print Solution().convert("ABCDEFGHIJKLMN",1)
    print Solution().convert("ABCDEFGHIJKLMN",2)
    print Solution().convert("ABCDEFGHIJKLMN",3)
    print Solution().convert("ABCDEFGHIJKLMN",4)
    print Solution().convert("ABCDEFGHIJKLMN",5)
