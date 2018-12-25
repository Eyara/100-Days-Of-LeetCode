class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = list()
        for i in s:
            result.append(i)
            if len(set(result)) < len(result):
                result.pop(0)
        return len(result)
