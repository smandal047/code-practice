class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        sort_s = sorted(s)
        sort_t = sorted(t)

        if sort_s == sort_t:
            return True
        else:
            return False