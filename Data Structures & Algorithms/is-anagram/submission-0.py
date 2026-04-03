class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        res=0
        if len(s)==len(t):

            for i in range(len(s)):
                if sorted_s[i] == sorted_t[i]:
                    res+=1
                if res == len(s) and res == len(t):
                    return True
            return False

        return False