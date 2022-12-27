"""
https://leetcode.com/problems/integer-to-english-words/description/
"""

class Solution:
    def numberToWords(self, num: int) -> str:

        if num is None or num == 0:
            return "Zero"

        to_19 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",      "Ten", "Eleven", "Twelve",  "Thirteen",  "Fourteen", "Fifteen","Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
        tens = ["", "Ten", "Twenty " , "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        def helper(num: int) -> str:
            if num < 20:
                s = to_19[num]
            elif num < 100:
                s = tens[ num // 10] + to_19[ num % 10 ]
            elif num < 1000:
                s = helper(num // 100), " Hundred and ", helper(num % 100)
            elif num < 1000000:
                s = helper(num // 1000), "Thousand and ", helper(num%1000)
            elif num < 1000000000:
                s = helper(num // 1000000), "Million and ", helper(num % 1000000)
            else:
                s = helper(num // 1000000000), " Billion and ", helper(num % 1000000000)
            return s.strip()
        return helper(num)
    