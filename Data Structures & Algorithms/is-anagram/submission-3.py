from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if Counter(s) == Counter(t):
            return True
        return False