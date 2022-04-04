# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        new_list=[]
        for i in strs:
            new="".join(sorted(i))
            if new in dic:
                dic[new]+=[i]
            else:
                dic[new]=[i]
        
        return dic.values()
