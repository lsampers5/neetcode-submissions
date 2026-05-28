class Solution:

    def encode(self, strs: List[str]) -> str: #take a list of strings mash them together (with a key to undo them)
        #The goal is to turn a list like ["Hello", "World"]
        #into "2/5/5/HelloWorld"
        #The key for this is #ofwords/letters in first word/ letters in second word / all words cramed together

        encodedString = str(len(strs)) + "/"
        combined = ""
        for s in strs:
            encodedString += str(len(s)) + "/"
            combined += s
        
        encodedString = encodedString + combined
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        i = 0 # Pointer

         # Meta data section
        slash = s.find("/", i)
        numWords = s[i : slash]
        i = slash + 1

        wordLengths = []
        for words in range(int(numWords)):
            slash = s.find("/", i)
            wordLengths.append(int(s[i:slash]))
            i = 1 + slash
        print(wordLengths)

         # Pay load section
        decodedStrings = []
        for length in wordLengths:
            decodedStrings.append(s[i:i + int(length)])
            i = i + length
        
        return decodedStrings
