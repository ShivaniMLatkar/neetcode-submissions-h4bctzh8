class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = ''
        for _ in s:
            if _.isalnum():
                clean_str += _.lower()
        
        return clean_str == clean_str[::-1]
        