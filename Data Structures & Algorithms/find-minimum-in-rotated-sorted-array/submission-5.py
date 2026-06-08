class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        mid = len(nums) // 2
        r = len(nums) - 1
        l = 0
        if nums[l] < nums[r]:
            return nums[l]
    
        while l <= r:
            mid = (r + l) // 2
            if nums[mid] < nums[r]:
                r = mid


            elif nums[mid] > nums[r]:
                l = mid + 1

            else:
 
                return nums[mid]



        mid = (r + l) // 2
        return nums[mid]
            
        



        