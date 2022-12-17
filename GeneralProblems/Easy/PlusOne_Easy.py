"""
https://leetcode.com/problems/plus-one/description/
"""

class Solution(object):
    def plusOne(self, digits):
        new_digit = int(''.join(str(x) for x in digits))
        new_value = new_digit + 1
        return [int(x) for x in str(new_value)]

