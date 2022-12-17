"""
https://leetcode.com/problems/longest-common-prefix/
"""

class solution(object):
    output = ""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return output

        # Find the minimum length string from the array
        minimumLength = len(strs[0])
        for i in range(1, len(strs)):
            minimumLength = min(minimumLength, len(strs[i]))

        # loop only till the min length
        for i in range(0, minimumLength):
            current = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return output
            output += current
        return output