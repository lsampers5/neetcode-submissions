class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict = {}
        if len(s) != len(t):
            return False

        for c in s:
            dict[c] = dict.get(c, 0) + 1

        for c in t:
            dict[c] = dict.get(c, 0) - 1
        

        for values in dict.values():
            if values != 0:
                return False

        return True
        
            
        