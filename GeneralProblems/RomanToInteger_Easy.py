"""
https://leetcode.com/problems/roman-to-integer/
"""

class Solution:
    def romanToInt(self, s: str):
        roman_values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        ans = 0
        for i in range(len(s)-1,-1,-1):
            num = roman_values[s[i]]
            if 4 * num < ans: ans -= num
            else: ans += num
        return ans

    

"""
Idea
The roman numbers when adding small values are written in 3 values at max
III = 3
XXX = 30

But for the 4th value then negate it from higher value
IV = 4
XL = 40

i.e., when subtracting, a smaller numbers appears to left of a larger number.

To work with this, we go from right to left, so range is higher to lower
    len(s) - 1 to -1, reducing by -1.

Since roman values increase by 5x, we can mutiply the left value by 4, if the 4x value is less then, subtract else add.

"""

# =========================
"""
Best Solution

If prev value is larger, then subtract, else add.
But issue with this is if IIII is given it'll take it as 4.
"""

class Solution(object):
    def romanToInt(self, s):
        roman_values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total, prev = 0,0
        for x  in reversed(s):
            if roman_values[x] < prev:
                total -= roman_values[x]
            else: total += roman_values[x]
            prev = roman_values[x]
        return total