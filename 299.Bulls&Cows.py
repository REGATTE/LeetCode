"""
https://leetcode.com/problems/bulls-and-cows/?envType=study-plan&id=level-1
"""
from operator import eq
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(map(eq, secret, guess))
        cows = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        return '%dA%dB' % (bulls, cows - bulls)

"""
operator.eq -> Function to check if a == b, and applied by map function

operator.le(a,b) -> a<=b
operator.lt(a,b) -> a<b
operator.ge(a,b) -> a>=b
operator.gt(a,b) -> a>b
operator.ne(a,b) -> a!=b
operator.eq(a,b) -> a==b
"""