class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        if r == 0 and target == nums[0]:
            return 0

        while l <= r:
            if l == r:
                if nums[l] != target:
                    return -1
                else:
                    return l
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[l]: # That means the left side is sorted 100p
                if nums[l] <= target and nums[mid] >= target:
                    # Okay so this means that if true target is between these two numbers which would be nice
                    r = mid
                else:
                    l = mid + 1
            elif nums[mid] < nums[r]: # right side is sorted
                if target <= nums[r] and nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            else:
                    l = mid + 1
                
        return -1

        