class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count1 = {}

        count2 = {}

        for c in s:
            count1[c] = count1.get(c, 0) + 1


        for c in t:
            count2[c] = count2.get(c, 0) + 1

        return count1 == count2

        