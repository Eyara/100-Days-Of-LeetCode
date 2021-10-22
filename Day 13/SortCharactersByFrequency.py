"""
Link: https://leetcode.com/problems/sort-characters-by-frequency/

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is
the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        result_str = ""
        freq_dict = {}
        for ch in s:
            if ch in freq_dict:
                freq_dict[ch] += 1
            else:
                freq_dict[ch] = 1
        ordered_freq_dict = dict(reversed(sorted(freq_dict.items(), key=lambda item: item[1])))

        for key in ordered_freq_dict:
            result_str += (key * ordered_freq_dict[key])

        return result_str


"""
RESULT

Runtime: 52 ms, faster than 60.97% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 15.5 MB, less than 60.51% of Python3 online submissions for Sort Characters By Frequency.
"""
