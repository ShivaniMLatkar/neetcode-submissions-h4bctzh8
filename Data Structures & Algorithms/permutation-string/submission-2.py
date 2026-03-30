class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s2)
        x=len(s1)
        c=0
        while x<=n:
            ws=s2[c:x]
            if sorted(ws)==sorted(s1):
                return True
            c+=1
            x+=1
        return False