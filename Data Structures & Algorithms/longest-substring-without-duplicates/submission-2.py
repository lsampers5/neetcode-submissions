class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0

        seen = set()
        if len(s) == 0:
            return 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            length = max(length, len(seen))

        return length


        