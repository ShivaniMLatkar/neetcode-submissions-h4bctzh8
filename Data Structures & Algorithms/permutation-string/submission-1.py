class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s1_set = set(s1)
        n = len(s1)
        for i in range(len(s2)-n+1):
           if s2[i] in s1_set:
                subStr = s2[i:(i+n)]
                if sorted(subStr) == s1:
                    return True
        return False