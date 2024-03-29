"""
Link: https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words.
The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = [x.strip() for x in s.split(" ") if len(x.strip()) > 0]
        print(words)
        return ' '.join(words[::-1])


"""
RESULT

Runtime: 48 ms, faster than 32.39% of Python3 online submissions for Reverse Words in a String.
Memory Usage: 14.3 MB, less than 86.72% of Python3 online submissions for Reverse Words in a String.
"""
