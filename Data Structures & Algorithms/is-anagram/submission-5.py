class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict = {}

        for c in s:
            dict[c] = dict.get(c, 0) + 1

        for c in t:
                dict[c] = dict.get(c, 0) - 1

        for values in dict.values():
            if values != 0:
                return False

        return True
        
            
        