class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #step 1 - create result & temp

        result = []
        temp = []

        i = len(strs) - 1
        
        while i >= 0: 


            j = 0   #j goes back to 0 this is just going to hold the starting index

            while i > j:

                if (len(strs[j]) != len(strs[i])):
                    j += 1
                    continue

                if (self.isAnagram(strs[j], strs[i])):
                    temp.append(strs[j])
                    strs.pop(j)
                    j -= 1
                    i -= 1

                j += 1

            temp.append(strs[i])
            strs.pop(i)
            i -= 1
            result.append(temp.copy())
            temp.clear()
    
        return result
            

        

    def isAnagram(self, s: str, t: str):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for c in t:
            freq[c] = freq.get(c, 0) - 1
        
        for value in freq.values():
            if value != 0:
                return False
        
        return True

        