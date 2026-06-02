class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        need = 0
        for char in t:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] == 1:
                need += 1


        left = 0
        right = 0
        have = 0
        best = s
        result =""
        check = False

        for char in s:
            right += 1
            if char in freq:
                freq[char] -= 1
                if freq[char] == 0:
                    have += 1
            
            while have == need: # When window is valid
                if len(best) >= len(s[left : right]):
                    best = s[left : right]
                    check = True
                if s[left] in freq:
                    freq[s[left]] += 1
                    if freq[s[left]] == 1: 
                        have -= 1
                left += 1
                print(best)
        print(check)
        if check == True:
            result = best
        return result


