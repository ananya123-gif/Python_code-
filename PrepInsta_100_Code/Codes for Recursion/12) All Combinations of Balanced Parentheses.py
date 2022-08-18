# All Combinations of Balanced Parentheses

# Input : n=1
# Output: {}

# Input : n=2
# Output: {}{} {{}}

# Input : n=3
# Output: {{}}{} {{{}}} {}{}{} {}{{}} {{}{}}

def generateParenthesis(n, Open, close, s, ans):
    if Open == n and close == n:
        ans.append(s)
        return
    if Open < n:
        generateParenthesis(n, Open + 1, close, s + "{", ans)
    if close < Open:
        generateParenthesis(n, Open, close + 1, s + "}", ans)

n = int(input())
ans = []
generateParenthesis(n, 0, 0, "", ans)
for s in ans:
    print(s)
