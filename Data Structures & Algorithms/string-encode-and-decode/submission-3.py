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

    def decode(self, s: str) -> List[str]: #take the encoded string and return the list
        #so we have "2/5/5/HelloWorld"
        #What do we do now chat
        



        numWords = int(s[0:s.find("/")]) #Gets num words
        s = s[(s.find("/") + 1):]
        #Need lengths specifically need numWords amount of lengths
        wordLengths = []
        for num in range(numWords):
            length = s[0:s.find("/")] # gets length
            s = s[s.find("/") + 1:] # gets rest of string without 3/
            wordLengths.append(int(length))
        print(wordLengths)
        # Now we should have only combined strings left in the encoded string
        #We can use the array of lengths to combine it all together lets go

        decodedStrings = []
        for length in wordLengths:
            word = s[0:length]
            decodedStrings.append(word)

            s = s[length:]
        


        return decodedStrings
