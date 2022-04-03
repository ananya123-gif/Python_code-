# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ws=0
        max_length=0
        hash_map={}
        for we in range(len(s)):
            curr_char=s[we]
            if curr_char in hash_map:
                ws=max(ws,hash_map[curr_char]+1)
            hash_map[curr_char]=we
            max_length=max(max_length,we-ws+1)
        return max_length
