class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Step 1 - Find potential starts
        if len(nums) == 0:
            return 0

        map = {}
        # Key - num
        # Value - index

        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i


        # Step 2 - Find the potential starters
        potentialStarters = []
        for num in map:
            if (num - 1) not in map:
                potentialStarters.append(num)
        
        # Step 3 - Find the length of the streaks
        i = 1
        j = 0
        streak = []
        while j < len(potentialStarters):
            num = potentialStarters[j]
            

            if num + i in map:
                i = i + 1
                streak.append(i)
            else:
                i = 1
                streak.append(i)
                j = j + 1

        return max(streak)






            





