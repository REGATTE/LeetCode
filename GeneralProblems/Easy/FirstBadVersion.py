"""
https://leetcode.com/problems/first-bad-version/description/
"""

class Solution(object):
    def firstBadVersion(self, n: int) -> int:
        # if number of version are 1, then return 1
        if n == 1:
            return 1
        # define oldest and latest versions
        oldestVersion = 1
        latestVersion = n

        while oldestVersion < latestVersion:
            midVersion = oldestVersion + (latestVersion - oldestVersion)/2
            if isBadVersion(midVersion): latestVersion = midVersion
            else: oldestVersion = midVersion + 1
        return oldestVersion

        