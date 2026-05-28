class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # First instinct use a counter
        
        # Plan we do not want to waste time looking at things 
        # that cannot be the start of a sequence

        #Step 1 - Find potential starts

        map = {}
        # Key - num
        # Value - index

        # Things to keep in consideration
        # 1 - Make sure if there is two of the same numbers it will still wokr


        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = i

        # Now we are chillen with a map

        # Find which numbers touch
        # Somehow need to find the smallest number that works
        potentialStarters = []
        for num in map:
            if (num - 1) not in map:
                potentialStarters.append(num)
        

#Now we are chillen with a map and potential starts of the longest sequence
        # Take potential starts and explore perhaps
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

        if len(streak) == 0:
            return 0
        return max(streak)






            





