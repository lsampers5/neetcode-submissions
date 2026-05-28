class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}
        # key = sorted word
        # value = list of anagrams

        for str in strs:
            key = "".join(sorted(str))

            if key not in groups:
                groups[key] = []

            groups[key].append(str)
        
        result = []
        for key in groups:
            result.append(groups[key])

        return result