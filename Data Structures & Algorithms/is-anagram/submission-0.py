class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_s = sorted(s)
        str_t = sorted(t)
        if len(str_s) == len(str_t):
            for i in range(len(str_s)):
                if str_s[i] == str_t[i]:
                    pass
                else:
                    return False
            return True
        return False                
        