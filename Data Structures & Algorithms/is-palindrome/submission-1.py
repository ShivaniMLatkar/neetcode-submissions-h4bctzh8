class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = ''
        for _ in s:
            if _.isalnum():
                new_str += _.lower()
        
        l = 0
        r = len(new_str)-1
        
        while l<=r:
            if new_str[l] != new_str[r]:
                return False
            l+=1
            r-=1
            
        return True