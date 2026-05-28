class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        result = []

        for i in range(len(nums)):
            c = target - nums[i]
            if nums[i] in dict:
                result.append(dict[nums[i]])
                result.append(i)
                return result
            dict[c] = i

     



        




        
        