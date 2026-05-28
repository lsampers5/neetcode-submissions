class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        #We have a freq table
        #key = num
        #value = freq

        #Now we need to take the k highest frequencies
        result = []
        while k > 0:
            largest = max(freq, key = freq.get)
            result.append(largest)
            freq.pop(largest)
            k -= 1

        return result
            


                