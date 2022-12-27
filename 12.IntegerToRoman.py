"""
https://leetcode.com/problems/integer-to-roman/
"""

class Solution:
    def intToRoman(num):
        symbol = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]   
        value =  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        i = 0
        res = ""
        while num > 0:
            while (num >= value[i]):
                num -= value[i]
                res += symbol[i]
            i += 1
        print(res)

Solution.intToRoman(1900)