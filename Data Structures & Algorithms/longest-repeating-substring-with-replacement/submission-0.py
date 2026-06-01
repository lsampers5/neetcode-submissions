class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        windowSize = 0
        left = 0
        right = 0
        replacementsNeeded = 0
        length = 0


        for char in s:
            freq[char] = freq.get(char, 0) + 1
            right += 1
            windowSize = right - left
            mostFreq = max(freq.values())
            replacementsNeeded = windowSize - mostFreq

            while replacementsNeeded > k:
                print(left)
                freq[s[left]] = freq.get(s[left], 0) - 1
                left += 1
                windowSize = right - left
                mostFreq = max(freq.values())
                replacementsNeeded = windowSize - mostFreq
            length = max(windowSize, length)
        return length
                



            
            
            





        mostFreq = max(freq.values())

        replacementsNeeded = len(s) - mostFreq



                    # replacements needed to make the whole string correct would be len(s) - mostFreq 
                    # So then if not that I guess create a window
                    # use right and expand and replace as needed
                    # Once the replacements run out then we move our left pointer
                    # until we get a replacement back 
                    # How will we know if we get a replacement back?
                    # update freq table apparently
                    # While saving the max length we achieved before running out of string

