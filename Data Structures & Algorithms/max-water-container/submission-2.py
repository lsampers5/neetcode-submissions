class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #What is the plan

        # Governing equation: i2 - i1 * min(nums[i2], nums[i1]) = num

        # Goal is maximize the equation from the numbers given
        left = 0
        right = len(heights) - 1
        result = 0



        while left < right:

            area = (right - left) * min(heights[right], heights[left])

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
            
            result = max(result, area)

        return result


            
            
             


