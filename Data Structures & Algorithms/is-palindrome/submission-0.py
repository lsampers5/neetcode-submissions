class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Steps
        # Make all lowercase
        # cut out spaces
        # cut out characters that are not letter/numbers
        
        s = s.lower()
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c)
        
        back = len(chars) - 1
        front = 0
        while back > front:
            if (chars[back] != chars[front]):
                return False
            back -= 1
            front+= 1
        
        return True

