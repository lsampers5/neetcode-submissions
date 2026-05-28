import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        heap = [] 

        for key in freq:
            heapq.heappush(heap, (-freq[key], key))
        
        result = []
        while k > 0:
            (freq, num) = heapq.heappop(heap)
            result.append(num)
            k -= 1

        return result