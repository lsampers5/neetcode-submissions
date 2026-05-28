class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Cleaning up logic in step 3
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
        streaks = []
        for starter in potentialStarters:
            streak = 1
            while starter + streak in map:
                streak = streak + 1
            streaks.append(streak)
            
        return max(streaks)






            





