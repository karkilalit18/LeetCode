class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        res = []
        order = -1
        for i in range(len(groups)):
            if groups[i] != order:
                order = groups[i]
                res.append(words[i])
        return res