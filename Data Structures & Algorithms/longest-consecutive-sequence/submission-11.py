class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        
        longest = 0

        for num in numsSet:

            if num - 1 not in numsSet:

                streak = 1

                while (num + streak) in numsSet:
                    streak += 1

                longest = max(longest, streak)
        
        return longest