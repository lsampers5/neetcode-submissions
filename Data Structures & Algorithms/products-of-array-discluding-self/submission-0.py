class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force
        result = []
        i = 0
        while  len(nums) > i:
            sum = 1
            j = 0
            while len(nums) > j:
                if j == i:
                    j = j + 1
                    continue
                sum = sum * nums[j]
                j = j + 1
            result.append(sum)
            i = i + 1


        return result
        