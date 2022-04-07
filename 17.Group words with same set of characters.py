# Given a list of words with lower cases. Implement a function to find all Words that have the same unique character set . 
# Example:  
# Input: words[] = { "may", "student", "students", "dog", "studentssess", "god", "cat", "act", "tab", "bat", "flow", "wolf", "lambs",
#                  "amy", "yam", "balms", "looped", "poodle"};

# Output : 
# looped, poodle, 
# lambs, balms, 
# flow, wolf, 
# tab, bat, 
# may, amy, yam, 
# student, students, studentssess, 
# dog, god, 
# cat, act, 

# All words with same set of characters are printed together in a line.

from collections import Counter

def group_words(inp_list):
    d={}
    for word in inp_list:
        wordDict = Counter(word)
        key = wordDict.keys()
        key = sorted(key)
        key = ''.join(key)
        if key in d.keys():
            d[key].append(word)
        else:
            d[key]=[]
            d[key].append(word)
    for (key,value) in d.items():
        print(','.join(d[key]))

inp_list=['may','student','students','dog','studentssess','god',
          'cat','act','tab','bat','flow','wolf','lambs','amy','yam','balms','looped','poodle']
group_words(inp_list)
