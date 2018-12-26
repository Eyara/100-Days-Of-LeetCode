class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if self.isPalindrome(s):
            return s
        result = ''
        for i in range(len(s), 0, -1):
            for j in range(len(s) + 1 - i):
                if self.isPalindrome(s[j:j + i]) and len(result) < len(s[j:j + i]):
                    result = s[j:j + i]
        
        return result
        
    def isPalindrome(self, s):
        return s == s[::-1]
