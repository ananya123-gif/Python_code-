# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        p = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                p.append((i,i+1))
            if i<len(s)-2 and s[i] == s[i+2]:
                p.append((i,i+2))
        sol = [0, 0]
        l = 1
        for i,j in p:
            while i>0 and j<len(s)-1 and s[i-1] == s[j+1]:
                i -= 1
                j += 1        
            if j-i+1 > l:
                sol[0] = i
                sol[1] = j
                l = j-i+1
        return s[sol[0]:sol[1]+1]
    
