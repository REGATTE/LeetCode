"""
https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left-1, right)
            if right > left: 
                generate(p + ')', left, right-1)
            if not right:
                parens += p,
            print(parens)
        return generate('', n, n)

"""
First add a left bracket, 
then add a right bracket, 
n - 1 from both.
Recursive till n = 0
"""

Solution.generateParenthesis(3)