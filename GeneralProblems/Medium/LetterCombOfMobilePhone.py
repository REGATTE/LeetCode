"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

class Solution(object):
    DIGIT_DICT = {
        "2" : ['a', 'b', 'c'],
        "3" : ['d', 'e', 'f'],
        "4" : ['g', 'h', 'i'],
        "5" : ['j', 'k', 'l'],
        "6" : ['m', 'n', 'o'],
        "7" : ['p', 'q', 'r', 's'],
        "8" : ['t', 'u', 'v'],
        "9" : ['w', 'x', 'y', 'z']
    }
    
    def letterCombinations(self, digits, letters="", pointer=0):
        if len(digits) == 0:
            return []
        if pointer == len(digits):
            return [letters]
        next_chars = self.DIGIT_DICT[digits[pointer]]
        new_strings = []
        for x in next_chars:
            new_strings.extend(iter(self.letterCombinations(letters=letters + x, digits=digits, pointer=pointer + 1)))
        return new_strings



"""
=============================
"""

class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if digits == "":
            return[]
        numbers = list(phone_map[digits[:1]])
        for digit in digits[1:]:
            numbers = [old + new for old in numbers for new in list(phone_map[diigit])]
        return numbers