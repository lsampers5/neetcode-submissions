class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        back = len(s) - 1
        front = 0

        while front < back:

            if not s[front].isalnum():
                front += 1
                continue

            elif not s[back].isalnum():
                back -= 1
                continue
            
            if s[front].lower() == s[back].lower():
                back -= 1
                front += 1
            else:
                return False
            
            
        return True
            
