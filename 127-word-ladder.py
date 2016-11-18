# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

#   1 Only one letter can be changed at a time
#   2 Each intermediate word must exist in the word list

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        from collections import defaultdict
        wordList = list(wordList) 
        wordList = [beginWord] + wordList + [endWord]
        dict = defaultdict(set)
        for word in wordList:
            for char in map(chr,range(97,123)):
                for i in range(len(word)):
                    child = word[:i] + char + word[i+1:]
                    if child not in dict and child in wordList and child != word: dict[word].add(child)
#        return dict
        res = [[beginWord]]
        step = 1
        while res and res[0][-1] != endWord:
            res = [r + [p] for r in res for p in dict[r[-1]]]
            print res
            step +=1
        return step
        
    def hamming(self, str1, str2):
        import itertools
        return sum(c1 != c2 for c1, c2 in itertools.izip(str1, str2))

if __name__ == "__main__":
#    print Solution().ladderLength("hit","cog",set(["hot","dot","dog","lot","log"]))
    print Solution().ladderLength("a","c",set(["a","b","c"]))
